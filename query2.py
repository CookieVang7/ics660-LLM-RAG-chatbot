from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from transformers import BartForConditionalGeneration, BartTokenizer
from transformers import AutoTokenizer, AutoModelForCausalLM
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
    results = collection.query(query_embeddings=[query_embedding], n_results=2)

    for result in results['documents'][0]:
        print('RESULT')
        print(result)

    return results

def generate_answer_with_llm(query, context_chunks, model_name="facebook/bart-large-cnn"):
    # Load the LLM and tokenizer
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    # Prepare the input for the model
    context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])
    input_text = f"Question: {query}\n\nContext: {context}"

    # tokenize input
    inputs = tokenizer(input_text, return_tensors='pt', max_length=512, truncation=True)

    # Generate the response
    summary_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=2, early_stopping=True)
    answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return answer

def ssa(query, response, model_name="microsoft/DialoGPT-medium"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

        # Add pad token if not already present
    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        model.resize_token_embeddings(len(tokenizer))

    evaluation_prompt = f"""
    On a scale of 0 to 1 with 1 being the highest, give a score on the sensibility and specificity of the query and response

    Query: {query}
    Response: {response}
    """

    inputs = tokenizer(evaluation_prompt, return_tensors="pt", max_length=1024, truncation=True, padding = "max_length")
    # if inputs['input_ids'].shape[1] > 1024:
    #     inputs = tokenizer(evaluation_prompt, return_tensors="pt", max_length=1024, truncation=True)
    attention_mask = inputs['input_ids'] != tokenizer.pad_token_id
    print("Tokenized inputs:", inputs)

    # Generate the response
    outputs = model.generate(
        inputs["input_ids"],
        max_length=2048,
        attention_mask=attention_mask,
        num_beams=5,
        no_repeat_ngram_size=2,
        early_stopping=True,
        pad_token_id=tokenizer.pad_token_id
    )
    print('OUTPUT: ', outputs)
    evaluation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return evaluation

def main():
    query = input("Enter a query about Agile: ")
    chroma_path = "C:\\Users\\cooki\\OneDrive\\Documents\\Metro State Stuff\\660-Master's Thesis\\ics660-LLM-RAG-chatbot\\chroma"
    collection_name = 'markdown_embeddings'

    # Query the vector database
    # "results" returns: ids, distances, metadatas, embeddings, documents, uris, data, included
    results = query_vector_database(query, chroma_path, collection_name)
    
    # Extract the context chunks from results["documents"][0] which holds all the k retrieved chunks
    context_chunks = [chunk for chunk in results["documents"][0]]

    # Generate an answer with the LLM
    answer = generate_answer_with_llm(query, context_chunks)

    evaluation = ssa(query,answer)
    print('SSA RESPONSE')
    print(evaluation)

    print(f"Query: {query}")
    print(f"Answer: {answer}")

if __name__ == '__main__':
    main()


# some thoughts:

# What if the markdown file is the problem? Try having just text instead of all those links and such
# Try using different LLMs
# Try chunking multiple markdown files and putting that into chroma 