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

def generate_answer_with_llm(query, context_chunks, model_name="distilbert-base-uncased-distilled-squad"):
    # Load the LLM and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)

    # Prepare the input for the model
    context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])
    inputs = tokenizer.encode_plus(query, context, add_special_tokens=True, return_tensors='pt', max_length=512, truncation=True)
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    # Generate the response
    outputs = model(input_ids, attention_mask=attention_mask)
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1

    # Decode the response
    answer = tokenizer.decode(input_ids[0][answer_start:answer_end], skip_special_tokens=True)

    return answer

def main():
    query = "What is Agile software development?"
    chroma_path = "C:\\Users\\cooki\\OneDrive\\Documents\\Metro State Stuff\\660-Master's Thesis\\ics660-LLM-RAG-chatbot\\chroma"
    collection_name = 'markdown_embeddings'

    # Query the vector database
    results = query_vector_database(query, chroma_path, collection_name)

    print(results)
    print(results['ids'])

    for result in results:
        print(result)

    #results["metadatas"]
    
    # Extract the context chunks from the results
    context_chunks = [chunk for chunk in results["metadatas"]]

    # Generate an answer with the LLM
    answer = generate_answer_with_llm(query, context_chunks)

    print(f"Query: {query}")
    print(f"Answer: {answer}")

if __name__ == '__main__':
    main()