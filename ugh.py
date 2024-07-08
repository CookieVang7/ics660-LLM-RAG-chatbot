import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import chromadb
import numpy as np
import json

# Function to read the markdown file
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def main():
    file_path = 'knowledge_base/root_article/Agile_software_development.md'
    text = read_markdown_file(file_path)

    # Step 1: Chunk the text using LangChain's text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    chunks = text_splitter.split_text(text)

    # Step 2: Create embeddings using LangChain's HuggingFaceEmbeddings
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'  # Sentence-BERT model
    embeddings_model = HuggingFaceEmbeddings(model_name=model_name)

    #embeddings = [embeddings_model.embed(chunk) for chunk in chunks]
    embeddings = embeddings_model.embed_documents(chunks)

    # Step 3: Store embeddings in Chroma
    chroma_client = chromadb.Client()

    collection_name = 'markdown_embeddings'
    collection = chroma_client.get_or_create_collection(name=collection_name)

    ids = [f'doc_chunk_{i}' for i in range(len(chunks))]
    metadata = [{'chunk': chunk} for chunk in chunks]

    # Add embeddings to Chroma collection
    collection.add(ids=ids, embeddings=embeddings, metadatas=metadata, documents=chunks)

    #embedding_list = []

    #ids = [f'doc_chunk_{i}' for i in range(len(chunks))]

    # for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
    #     embedding_set = {
    #         'id': f'doc_chunk_{i}',  # Ensure id is a string
    #         'vector': embedding.tolist() if isinstance(embedding, np.ndarray) else embedding,  # Ensure vector is a list
    #         'metadata': {'chunk': chunk}
    #     }
    #     embedding_list.append(embedding_set)

    # #collection.add(embedding_sets)
    # #collection.add(embedding_list)
    # embedding_list_json = json.dumps(embedding_list)
    # collection.add(embedding_list_json)

    print("Embeddings stored in Chroma database.")

if __name__ == '__main__':
    main()