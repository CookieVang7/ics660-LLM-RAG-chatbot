import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from transformers import BartForConditionalGeneration, BartTokenizer
from bert_score import score as bert_score
from rouge_score import rouge_scorer

def generate_answer_with_llm1(query, model_name="facebook/bart-large-cnn"): # summarization model
    # Load the LLM and tokenizer
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    # Prepare the input for the model
    input_text = f"User: {query}"

    print('INPUT TEXT')
    print(input_text)

    # Tokenize input
    inputs = tokenizer(input_text, return_tensors='pt', max_length=1024, truncation=True)

    # Generate the response
    summary_ids = model.generate(inputs['input_ids'], max_new_tokens=100, num_beams=2, early_stopping=True)
    answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return answer

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

        # Generate an answer with the LLM
        answer = generate_answer_with_llm1(query)
        answer = answer.replace(f"User:","")
        answer = answer.replace(f"user:","")
        answer = answer.replace(query,"")

        st.write(f"**User:** {query}")
        st.write(f"**Assistant:** {answer}")

        if reference_answer:
            P, R, F1 = bertscore([answer], [reference_answer])
            rouge1_scores = rouge1([answer], [reference_answer])
            st.write(f"BERTScore F1: {F1[0].item():.6f}")
            st.write(f"ROUGE-1 F1 Score: {rouge1_scores[0]:.6f}")