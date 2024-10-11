from langchain_huggingface import HuggingFaceEmbeddings
import chromadb
from transformers import pipeline

# Initialize the embeddings model and Chroma client
embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db_path = "C:\\Users\\cooki\\OneDrive\\Documents\\Metro State Stuff\\660-Master's Thesis\\ics660-LLM-RAG-chatbot\\chroma\\chroma.sqlite3"
chroma_client = chromadb.PersistentClient(path=db_path)
collection = chroma_client.get_collection("markdown_embeddings")

# Function to query the database and get relevant chunks
def query_database(query, collection, embeddings_model, num_results=5):
    # Convert query to embeddings
    query_embeddings = embeddings_model.embed_query([query])[0]
    
    # Perform search in the collection
    results = collection.query(
        query_embeddings=[query_embeddings],
        n_results=num_results
    )
    
    # Extract relevant chunks
    relevant_chunks = [item["metadata"]["chunk"] for item in results["results"][0]["documents"]]
    return relevant_chunks

# Function to generate an answer from relevant chunks
def generate_answer(query, relevant_chunks):
    # Combine relevant chunks into a context
    context = " ".join(relevant_chunks)
    
    # Initialize the language model
    nlp_model = pipeline("question-answering")
    
    # Generate answer using the context
    answer = nlp_model(question=query, context=context)
    return answer["answer"]

# Example usage
query = "What is a mindset that drives software development practices?"
relevant_chunks = query_database(query, collection, embeddings_model)
answer = generate_answer(query, relevant_chunks)

print("MOOOO")
print("Answer:", answer)