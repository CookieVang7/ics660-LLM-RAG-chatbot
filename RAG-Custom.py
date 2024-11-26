import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
import chromadb
import torch
from bert_score import score as bert_score
from rouge_score import rouge_scorer
from customLLM import load_trained_model,encode,decode

device = 'cpu'
model = load_trained_model()

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

    return results

def generate_answer_with_customLLM(query,context_chunks):
    # Concatenate context chunks
    context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])

    # Prepare the input text for the custom language model
    input_text = f"Context: {context}\n\nUser: {query}"

    # Encode the input text
    input_encoded = torch.tensor([encode(input_text)], dtype=torch.long).to(device)

    print(f"Input shape before truncation: {input_encoded.shape}")

    # Truncate input to the maximum allowed length (block_size)
    if input_encoded.shape[1] > 256:  # Assuming block_size = 128 in language_model.py
        input_encoded = input_encoded[:, -256:]

    print(f"Input shape after truncation: {input_encoded.shape}")

    if input_encoded.shape[1] > 256:
        raise ValueError(f"Input sequence is too long! Length: {input_encoded.shape[1]} exceeds block_size")

    # Generate the response using the custom language model
    response_encoded = model.generate(input_encoded, max_new_tokens=100)

    # Decode the generated response
    response = decode(response_encoded[0].tolist())

    return response

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
        answer = generate_answer_with_customLLM(query,context_chunks)

        print(answer)

        answer = answer.replace(f"User: {query}","")

        st.write(f"**User:** {query}")
        st.write(f"**Assistant:** {answer}")

        if reference_answer:
            P, R, F1 = bertscore([answer], [reference_answer])
            rouge1_scores = rouge1([answer], [reference_answer])
            st.write(f"BERTScore F1: {F1[0].item():.6f}")
            st.write(f"ROUGE-1 F1 Score: {rouge1_scores[0]:.6f}")