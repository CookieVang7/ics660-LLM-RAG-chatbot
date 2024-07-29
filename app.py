import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from transformers import BartForConditionalGeneration, BartTokenizer, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM
import chromadb
import torch
from bert_score import score as bert_score
from rouge_score import rouge_scorer

def query_vector_database(query, chroma_path, collection_name):
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

    for result in results['documents'][0]:
        print('RESULT')
        print(result)
        print('')

    return results

def generate_answer_with_llm1(query, context_chunks, conversation_history, model_name="facebook/bart-large-cnn"):
    # Load the LLM and tokenizer
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    # Prepare the input for the model
    context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])
    history = " ".join([f"User: {q}\nAssistant: {a}" for q, a in conversation_history[-3:]])
    input_text = f"Context: {context}\n\n{history}\n\nUser: {query}\nAssistant:"

    # Tokenize input
    inputs = tokenizer(input_text, return_tensors='pt', max_length=1024, truncation=True)

    # Generate the response
    summary_ids = model.generate(inputs['input_ids'], max_new_tokens=100, num_beams=2, early_stopping=True)
    answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return answer

def generate_answer_with_llm2(query, context_chunks, conversation_history, model_name="tiiuae/falcon-7b-instruct"):
    # Load the LLM and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Prepare the input for the model
    context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])
    history = " ".join([f"User: {q}\nAssistant: {a}" for q, a in conversation_history[-3:]])
    input_text = f"Context: {context}\n\n{history}\n\nUser: {query}\nAssistant:"

    print('INPUT TO LLM:')
    print(input_text)

    # Tokenize input
    inputs = tokenizer(input_text, return_tensors='pt', max_length=1024, truncation=True)

    # Generate the response
    summary_ids = model.generate(inputs['input_ids'], max_new_tokens=100, num_beams=2, early_stopping=True)
    answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    if "Context:" in answer:
        answer = answer.split("Context:")[0].strip()

    if "User:" in answer:
        answer = answer.split("User:")[0].strip()

    return answer

# def generate_answer_with_llm2(query, context_chunks, conversation_history, model_name="Falconsai/text_summarization"):
#     # Load the LLM and tokenizer
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

#     # Prepare the input for the model
#     context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])
#     history = " ".join([f"User: {q}\nAssistant: {a}" for q, a in conversation_history[-3:]])
#     #input_text = f"Context: {context}\n\n{history}\n\nUser: {query}\nAssistant:"
#     input_text = f"User: {query}\nAssistant:"

#     print('INPUT TO LLM:')
#     print(input_text)

#     # Tokenize input
#     inputs = tokenizer(input_text, return_tensors='pt', max_length=1024, truncation=True)

#     # Generate the response
#     summary_ids = model.generate(inputs['input_ids'], max_new_tokens=100, num_beams=2, early_stopping=True)
#     answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#     if "Context:" in answer:
#         answer = answer.split("Context:")[0].strip()

#     if "User:" in answer:
#         answer = answer.split("User:")[0].strip()

#     return answer

# def generate_answer_with_llm2(query, context_chunks, model_name="Falconsai/text_summarization"):
#     # Load the LLM and tokenizer
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

#     if tokenizer.pad_token is None:
#         tokenizer.add_special_tokens({'pad_token': '[PAD]'})
#         model.resize_token_embeddings(len(tokenizer))

#     # Prepare the input for the model
#     context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])
#     input_text = f"Question: {query}\n\nContext: {context}"

#     # tokenize input
#     inputs = tokenizer(input_text, return_tensors='pt', max_length=512, truncation=True)

#     # Generate the response
#     summary_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=2, early_stopping=True)
#     answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#     return answer

def bertscore(candidates, references):
    P, R, F1 = bert_score(candidates, references, lang="en", verbose=True)
    return P, R, F1

def rouge1(candidates, references):
    scorer = rouge_scorer.RougeScorer(['rouge1'], use_stemmer=True)
    scores = [scorer.score(ref, cand) for ref, cand in zip(references, candidates)]
    rouge1_scores = [score['rouge1'].fmeasure for score in scores]
    return rouge1_scores

# Streamlit UI
st.title("Agile Chatbot")

chroma_path = "C:\\Users\\cooki\\OneDrive\\Documents\\Metro State Stuff\\660-Master's Thesis\\ics660-LLM-RAG-chatbot\\chroma"
collection_name = 'markdown_embeddings'

conversation_history = []

query = st.text_input("Enter a query about Agile (type 'quit' to exit):")
reference_answer = st.text_input("Enter reference answer to query: ")

if query and reference_answer:
    if query.lower() == 'quit':
        st.write("Session ended.")
    else:
        # Query the vector database
        results = query_vector_database(query, chroma_path, collection_name)

        # Extract the context chunks from results["documents"][0] which holds all the k retrieved chunks
        context_chunks = [chunk for chunk in results["documents"][0]]

        # Generate an answer with the LLM
        #answer = generate_answer_with_llm1(query, context_chunks, conversation_history)
        answer = generate_answer_with_llm2(query, context_chunks, conversation_history)

        # Update conversation history
        conversation_history.append((query, answer))
        if len(conversation_history) > 3:
            conversation_history.pop(0)  # Keep only the last 3 entries

        # Display the conversation history
        for q, a in conversation_history:
            st.write(f"**User:** {q}")
            st.write(f"**Assistant:** {a}")

        if reference_answer:
            P, R, F1 = bertscore([answer], [reference_answer])
            rouge1_scores = rouge1([answer], [reference_answer])
            st.write(f"BERTScore Precision: {P[0].item():.6f}")
            st.write(f"BERTScore Recall: {R[0].item():.6f}")
            st.write(f"BERTScore F1: {F1[0].item():.6f}")
            st.write(f"ROUGE-1 F1 Score: {rouge1_scores[0]:.6f}")