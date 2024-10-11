import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import chromadb
import torch
from bert_score import score as bert_score
from rouge_score import rouge_scorer
from sklearn.metrics.pairwise import cosine_similarity

def query_vector_database(query, chroma_path, collection_name):

    print('QUERYING VECTOR DATABASE FOR RELEVANT CHUNKS')

    # Load the embeddings model
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'  # Sentence-BERT model
    embeddings_model = HuggingFaceEmbeddings(model_name=model_name)

    # Embed the query
    query_embedding = embeddings_model.embed_query(query)

    # Initialize Chroma client
    chroma_client = chromadb.PersistentClient(path=chroma_path)

    # Retrieve the collection of vector embeddings
    collection = chroma_client.get_or_create_collection(name=collection_name)

    # Query the collection using vector search
    results = collection.query(query_embeddings=[query_embedding], n_results=2)

    retrieved_documents = results['documents'][0]
    squared_distances = results['distances'][0]
    print('SQUARED DISTANCE')
    print(squared_distances)

    # for i in range(2):
    #     print('RESULT')
    #     print(retrieved_documents[i])
    #     print('')
    #     if squared_distances[i] > 0.5:
    #         print('NOT RELEVANT')
    #         del retrieved_documents[i]
    #     else:
    #         print('YA, THEY RELEVANT')
    # Iterate over the documents and distances in reverse order
    for i in range(len(squared_distances) - 1, -1, -1):
        print('RESULT')
        print(retrieved_documents[i])
        print('')
        
        if squared_distances[i] > 0.5:
            print('NOT RELEVANT, DELETING')
            del retrieved_documents[i]  # Remove the document with distance > 0.5
        else:
            print('YA, THEY RELEVANT')

    return results

# def generate_answer(query, model_name="google/flan-t5-large"):
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

#     input_text = f"User: {query}\nAssistant:"

#     inputs = tokenizer(input_text, return_tensors='pt', max_length=1024, truncation=True)

#     summary_ids = model.generate(inputs['input_ids'], attention_mask=inputs['attention_mask'], max_new_tokens=100, num_beams=2, early_stopping=True)
#     answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#     print('generating answer')

#     return answer

def generate_answer_with_llm2(query, context_chunks, model_name="google/flan-t5-large", similarity_threshold=0.85): # Text2Text generation
    # Load the LLM and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Prepare the input for the model
    context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])
    #input_text = f"Context: {context}\nUser: {query}\nAssistant:"
    # input_text = (
    #     f"Use the following context to help answer the question. "
    #     f"Do not copy the context directly, but instead provide a new, original response based on it.\n\n"
    #     f"Context: {context}\n\n"
    #     f"User: {query}\nAssistant:"
    # )
    # input_text = (
    #     f"Context: {context}\n\n"
    #     f"User: {query}\n\n"
    #     f"Assistant: Please provide a concise and original summary based on the context, "
    #     f"answering the user's query. Do not simply repeat the context, but summarize it "
    #     f"and integrate it into a new response."
    # )
    # Chain of Thought Prompt
    input_text = (
        f"Context: {context}\n\n"
        f"User: {query}\n\n"
        f"Assistant: Let's break this down step by step. First, I'll check if the exact answer "
        f"to the question is found in the context provided. If it is, I will summarize the "
        f"relevant information instead of copying it. If not, I will use both the context and "
        f"my knowledge to generate a new, original response.\n\n"
    )

    print('INPUT TO LLM:')
    print(input_text)

    # Tokenize input
    inputs = tokenizer(input_text, return_tensors='pt', max_length=1024, truncation=True)

    # Generate the response
    summary_ids = model.generate(inputs['input_ids'], attention_mask=inputs['attention_mask'], max_new_tokens=150, num_beams=5, early_stopping=True)
    answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    model_name = 'sentence-transformers/all-MiniLM-L6-v2'  # Sentence-BERT model
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)

    context_embedding = embedding_model.embed_query(context)
    response_embedding = embedding_model.embed_query(answer)

    # Calculate cosine similarity between context and response
    similarity_score = cosine_similarity([context_embedding], [response_embedding])[0][0]
    print(f"Similarity score: {similarity_score}")

    if similarity_score > similarity_threshold:
        print("Response too similar to context. Regenerating with explicit summarization.")
        input_text = (
            f"Context: {context}\n\n"
            f"User: {query}\n\n"
            f"Assistant: The response was too similar to the context. Please provide a summarized and original answer."
        )
        inputs = tokenizer(input_text, return_tensors='pt', max_length=1024, truncation=True)
        summary_ids = model.generate(
            inputs['input_ids'], 
            attention_mask=inputs['attention_mask'], 
            max_new_tokens=150,
            num_beams=5,
            early_stopping=True
        )
        final_answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return final_answer

    if "Context:" in answer:
        answer = answer.split("Context:")[0].strip()

    if "User:" in answer:
        answer = answer.split("User:")[0].strip()

    if "Answer:" in answer:
        answer = answer.split("Answer:")[1].strip()

    return answer

# def bertscore(candidates, references):
#     P, R, F1 = bert_score(candidates, references, lang="en", verbose=True)
#     return P, R, F1

# def rouge1(candidates, references):
#     scorer = rouge_scorer.RougeScorer(['rouge1'], use_stemmer=True)
#     scores = [scorer.score(ref, cand) for ref, cand in zip(references, candidates)]
#     rouge1_scores = [score['rouge1'].fmeasure for score in scores]
#     return rouge1_scores

# Streamlit UI
st.title("Agile Chatbot")

chroma_path = "C:\\Users\\cooki\\OneDrive\\Documents\\Metro State Stuff\\660-Master's Thesis\\ics660-LLM-RAG-chatbot\\chroma"
collection_name = 'markdown_embeddings'

conversation_history = [] # CONVERSATION HISTORY DOES NOT WORK!!!!!!!!!!!!!!! FIX THIS NEXT SEMESTER

query = st.text_input("Enter a query about Agile (type 'quit' to exit):")
#reference_answer = st.text_input("Enter reference answer to query: ")

if query:
    if query.lower() == 'quit':
        st.write("Session ended.")
    else:
        # Query the vector database
        results = query_vector_database(query, chroma_path, collection_name)

        # Extract the context chunks from results["documents"][0] which holds all the k retrieved chunks
        context_chunks = [chunk for chunk in results["documents"][0]]

        # Generate an answer with the LLM
        #answer = generate_answer_with_llm1(query, context_chunks, conversation_history)
        answer = generate_answer_with_llm2(query, context_chunks)
        #answer = generate_answer(query)

        # Update conversation history
        # conversation_history.append((query, answer))
        # if len(conversation_history) > 3:
        #     conversation_history.pop(0)  # Keep only the last 3 entries
        st.write(f"**User:** {query}")
        st.write(f"**Assistant:** {answer}")


        # Display the conversation history
        # for q, a in conversation_history:
        #     st.write(f"**User:** {q}")
        #     st.write(f"**Assistant:** {a}")

        # if reference_answer:
        #     P, R, F1 = bertscore([answer], [reference_answer])
        #     rouge1_scores = rouge1([answer], [reference_answer])
        #     #st.write(f"BERTScore Precision: {P[0].item():.6f}")
        #     #st.write(f"BERTScore Recall: {R[0].item():.6f}")
        #     st.write(f"BERTScore F1: {F1[0].item():.6f}")
        #     st.write(f"ROUGE-1 F1 Score: {rouge1_scores[0]:.6f}")


# run app.py with 'streamlit run app.py'