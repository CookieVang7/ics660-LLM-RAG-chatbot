import tkinter as tk
from tkinter import scrolledtext
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from transformers import BartForConditionalGeneration, BartTokenizer
import chromadb

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot with History and Context")

        self.conversation_history = []

        self.create_widgets()
        
        self.chroma_path = "C:\\Users\\cooki\\OneDrive\\Documents\\Metro State Stuff\\660-Master's Thesis\\ics660-LLM-RAG-chatbot\\chroma"
        self.collection_name = 'markdown_embeddings'

    def create_widgets(self):
        self.query_label = tk.Label(self.root, text="Enter a query about Agile:")
        self.query_label.pack()

        self.query_entry = tk.Entry(self.root, width=100)
        self.query_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_query)
        self.submit_button.pack()

        self.history_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=100, height=20)
        self.history_box.pack()

    def query_vector_database(self, query):
        # Load the embeddings model
        model_name = 'sentence-transformers/all-MiniLM-L6-v2'  # Sentence-BERT model
        embeddings_model = HuggingFaceEmbeddings(model_name=model_name)

        # Embed the query
        query_embedding = embeddings_model.embed_query(query)

        # Initialize Chroma client
        chroma_client = chromadb.PersistentClient(path=self.chroma_path)

        # Retrieve the collection of vector embeddings
        collection = chroma_client.get_or_create_collection(name=self.collection_name)

        # Query the collection
        results = collection.query(query_embeddings=[query_embedding], n_results=5)

        return results

    def generate_answer_with_llm(self, query, context_chunks):
        # Load the LLM and tokenizer
        model_name = "facebook/bart-large-cnn"
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)

        # Prepare the input for the model
        context = " ".join([chunk for chunk in context_chunks if isinstance(chunk, str)])
        history = " ".join([f"User: {q}\nAssistant: {a}" for q, a in self.conversation_history[-3:]])
        input_text = f"{history}\nUser: {query}\n\nContext: {context}"

        # Tokenize input
        inputs = tokenizer(input_text, return_tensors='pt', max_length=512, truncation=True)

        # Generate the response
        summary_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=2, early_stopping=True)
        answer = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return answer

    def submit_query(self):
        query = self.query_entry.get()
        if query.lower() == 'quit':
            self.root.quit()
        else:
            # Query the vector database
            results = self.query_vector_database(query)

            # Extract the context chunks from results["documents"][0] which holds all the k retrieved chunks
            context_chunks = [chunk for chunk in results["documents"][0]]

            # Generate an answer with the LLM
            answer = self.generate_answer_with_llm(query, context_chunks)

            # Update conversation history
            self.conversation_history.append((query, answer))
            if len(self.conversation_history) > 3:
                self.conversation_history.pop(0)  # Keep only the last 3 entries

            # Display the conversation history
            self.history_box.delete(1.0, tk.END)
            for q, a in self.conversation_history:
                self.history_box.insert(tk.END, f"**User:** {q}\n")
                self.history_box.insert(tk.END, f"**Assistant:** {a}\n\n")

            self.query_entry.delete(0, tk.END)
            self.history_box.insert(tk.END, f"**Answer:** {answer}\n\n")

def main():
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()