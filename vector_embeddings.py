from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import chromadb
import os

def main():
    # Folder containing markdown files
    folder_path = 'knowledge_base/articles'  

    # Initialize Chroma client - pointing to /chroma diretory
    chroma_client = chromadb.PersistentClient(path="C:\\Users\\cooki\\OneDrive\\Documents\\Metro State Stuff\\660-Master's Thesis\\ics660-LLM-RAG-chatbot\\chroma")
    
    # Naming collection of vector embeddings as "markdown_embeddings"
    collection_name = 'markdown_embeddings'
    collection = chroma_client.get_or_create_collection(name=collection_name)

    # Initialize text splitter and embedding model
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'  # Sentence-BERT model from HuggingFace
    embeddings_model = HuggingFaceEmbeddings(model_name=model_name)
    
    all_chunks = []
    all_embeddings = []
    all_ids = []
    all_metadata = []

    # Iterate through all markdown files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            text = read_markdown_file(file_path)
            
            # Chunk the text using LangChain's text splitter
            chunks = text_splitter.split_text(text)
            
            # Create embeddings
            embeddings = embeddings_model.embed_documents(chunks)
            
            # Store the chunks, embeddings, ids, and metadata
            all_chunks.extend(chunks)
            all_embeddings.extend(embeddings)
            file_id = os.path.splitext(filename)[0]  # Use filename (without extension) as part of the ID
            all_ids.extend([f'{file_id}_chunk_{i}' for i in range(len(chunks))])
            all_metadata.extend([{'file': filename, 'chunk': chunk} for chunk in chunks])
    
    # Add all embeddings to Chroma collection
    collection.add(ids=all_ids, embeddings=all_embeddings, metadatas=all_metadata, documents=all_chunks)

    print("All embeddings stored in Chroma database.")

# Helper function to read a markdown file
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

if __name__ == '__main__':
    main()