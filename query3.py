from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
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

    # Retrieve the collection
    collection = chroma_client.get_or_create_collection(name=collection_name)

    # Query the collection
    results = collection.query(query_embeddings=[query_embedding], n_results=5)

    return results

def generate_answer_with_llm(query, context_chunks, model_name="bert-base-uncased"):
    # Load the LLM and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)

    # Prepare the input for the model
    context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])
    input_text = f"Question: {query}\n\nContext: {context}"

    # tokenize input
    inputs = tokenizer(input_text, return_tensors='pt', max_length=512, truncation=True)

    # Generate the response
    summary_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=2, early_stopping=True)
    answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return answer

def main():
    #query = "What is Agile software development?"
    query = input("Enter a query about Agile: ")
    chroma_path = "C:\\Users\\cooki\\OneDrive\\Documents\\Metro State Stuff\\660-Master's Thesis\\ics660-LLM-RAG-chatbot\\chroma"
    collection_name = 'markdown_embeddings'

    # Query the vector database
    results = query_vector_database(query, chroma_path, collection_name)

    #print(results)
    print('RESULTS DOCUMENT: ', results['documents'])
    print('RESULTS METADATAS: ', results['metadatas'])
    
    # Extract the context chunks from the results
    context_chunks = [chunk for chunk in results["metadatas"]]

    # Generate an answer with the LLM
    answer = generate_answer_with_llm(query, context_chunks)

    print(f"Query: {query}")
    print(f"Answer: {answer}")

if __name__ == '__main__':
    main()


# some thoughts:

# What if the markdown file is the problem? Try having just text instead of all those links and such
# Try using different LLMs
# Try chunking multiple markdown files and putting that into chroma 