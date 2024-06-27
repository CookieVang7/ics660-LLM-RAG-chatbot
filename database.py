from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
# from langchain.embeddings import OpenAIEmbeddings
# from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
import openai 
from dotenv import load_dotenv
import os
import shutil
import time

# loads environment variables
load_dotenv()
#openai.api_key = os.environ['OPENAI_API_KEY']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

CHROMA_PATH = 'chroma'
#ARTICLES = 'knowledge_base/articles'
ARTICLES = 'knowledge_base/root_article'

def main():
    generate_data_store()

# controls getting markdown files, splitting them into chunks and creating Chroma DB
def generate_data_store():
    docs = load_docs()
    #chunks = split_text(docs)
    save_to_chroma(docs)

# grabs the markdown files from the ARTICLES directory
def load_docs():
    loader = DirectoryLoader(ARTICLES, glob='*.md')
    docs = loader.load()
    return docs

def save_to_chroma(docs: list[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    max_retries = 10
    retry_delay = 2  # Start with a 2-second delay

    for attempt in range(max_retries):
        try:
            embeddings = []
            # Create embeddings for each document
            for doc in docs:
                model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model='gpt-3.5-turbo')
                response = model.predict(doc.page_content)
                embeddings.append(response['embedding'])

            # Save embeddings to Chroma
            db = Chroma.from_embeddings(
                embeddings, persist_directory=CHROMA_PATH
            )
            db.persist()
            print(f"Saved {len(docs)} documents to {CHROMA_PATH}.")
            return
        except Exception as e:
            if "Rate limit" in str(e) or "429" in str(e):
                print(f"Rate limit exceeded: {e}. Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(retry_delay)
                retry_delay *= 1.5  # Increase delay by 1.5x each retry
            else:
                print(f"An error occurred: {e}")
                break

    raise Exception("Max retries exceeded. Rate limit errors persist.")

# splits a list of Documents into chunks to make context of chunks more focused/relevant
# def split_text(docs: list[Document]):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000, # chunk size of 300 characters
#         chunk_overlap=500, # overlap between each chunk
#         length_function=len,
#         add_start_index=True,
#     )
#     chunks = text_splitter.split_documents(docs)
#     print(f"Split {len(docs)} documents into {len(chunks)} chunks.")

#     document = chunks[10]
#     print(document.page_content)
#     print(document.metadata)

#     return chunks

# # takes the chunks and uses OpenAI's embeddings() function to create the vector embeddings and saves it to the Chroma DB (a chroma.sqlite3 file)
# def save_to_chroma(chunks: list[Document]):
#     # Clear out the database first.
#     if os.path.exists(CHROMA_PATH):
#         shutil.rmtree(CHROMA_PATH)

#     max_retries = 10
#     retry_delay = 2  # Start with a 2-second delay

#     for attempt in range(max_retries):
#         try:
#             # Create a new DB from the documents.
#             db = Chroma.from_documents(
#                 chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
#             )
#             db.persist()
#             print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")
#             return
#         except Exception as e:
#             if "Rate limit" in str(e):
#                 print(f"Rate limit exceeded: {e}. Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
#                 time.sleep(retry_delay)
#                 retry_delay *= 1.5  # Increase delay by 1.5x each retry
#             else:
#                 print(f"An error occurred: {e}")
#                 break

#     raise Exception("Max retries exceeded. Rate limit errors persist.")


if __name__ == "__main__":
    main()