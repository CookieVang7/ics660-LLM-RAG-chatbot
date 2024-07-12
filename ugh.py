from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import chromadb

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

    embeddings = embeddings_model.embed_documents(chunks)

    #Step 3: Store embeddings in Chroma
    chroma_client = chromadb.PersistentClient(path="C:\\Users\\cooki\\OneDrive\\Documents\\Metro State Stuff\\660-Master's Thesis\\ics660-LLM-RAG-chatbot\\chroma")

    collection_name = 'markdown_embeddings'
    collection = chroma_client.get_or_create_collection(name=collection_name)

    ids = [f'doc_chunk_{i}' for i in range(len(chunks))]
    metadata = [{'chunk': chunk} for chunk in chunks]

    # Add embeddings to Chroma collection
    collection.add(ids=ids, embeddings=embeddings, metadatas=metadata, documents=chunks)

    print("Embeddings stored in Chroma database.")

if __name__ == '__main__':
    main()