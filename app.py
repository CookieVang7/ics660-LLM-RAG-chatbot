import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from transformers import BartForConditionalGeneration, BartTokenizer
import chromadb
import torch

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

    # Query the collection
    results = collection.query(query_embeddings=[query_embedding], n_results=5)

    return results

def generate_answer_with_llm(query, context_chunks, conversation_history, model_name="facebook/bart-large-cnn"):
    # Load the LLM and tokenizer
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    # Prepare the input for the model
    context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])
    history = " ".join([f"User: {q}\nAssistant: {a}" for q, a in conversation_history[-3:]])
    input_text = f"{history}\nUser: {query}\n\nContext: {context}"

    # Tokenize input
    inputs = tokenizer(input_text, return_tensors='pt', max_length=512, truncation=True)

    # Generate the response
    summary_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=2, early_stopping=True)
    answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return answer

# Streamlit UI
st.title("Agile Chatbot")

chroma_path = "C:\\Users\\cooki\\OneDrive\\Documents\\Metro State Stuff\\660-Master's Thesis\\ics660-LLM-RAG-chatbot\\chroma"
collection_name = 'markdown_embeddings'

conversation_history = []

query = st.text_input("Enter a query about Agile (type 'quit' to exit):")

if query:
    if query.lower() == 'quit':
        st.write("Session ended.")
    else:
        # Query the vector database
        results = query_vector_database(query, chroma_path, collection_name)

        # Extract the context chunks from results["documents"][0] which holds all the k retrieved chunks
        context_chunks = [chunk for chunk in results["documents"][0]]

        # Generate an answer with the LLM
        answer = generate_answer_with_llm(query, context_chunks, conversation_history)

        # Update conversation history
        conversation_history.append((query, answer))
        if len(conversation_history) > 3:
            conversation_history.pop(0)  # Keep only the last 3 entries

        # Display the conversation history
        for q, a in conversation_history:
            st.write(f"**User:** {q}")
            st.write(f"**Assistant:** {a}")

        st.write(f"**Answer:** {answer}")