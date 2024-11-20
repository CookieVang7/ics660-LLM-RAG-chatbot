# ics660-LLM-RAG-chatbot

This repo contains the source code for my master's thesis project, an LLM based chatbot using RAG. In addition to using out-of-the-box LLMs, a custom LLM is created and used by the chatbot.

The custom LLM is based off of freeCodeCamp.org's video about creating an LLM from scratch: https://www.youtube.com/watch?v=UU1WVnMk4E8.

Please note that the custom LLM currently does NOT work as intended.

## Architecture of Chatbot

![](https://github.com/CookieVang7/ics660-LLM-RAG-chatbot/blob/main/RAG%20implementation.png?raw=true)

## Key Implementation Points of Architecture
- Data Source: Wikipedia articles about Agile software development
- Chatbot UI: Streamlit (Python library)
- Embedding Model: sentence-transformers/all-MiniLM-L6-v2
- Out-of-the-box LLMs: facebook/bart-large-cnn and google/flan-t5-large
- Vector database: Chroma DB
- RAG mechanism: Langchain

## Libraries and Dependencies

See requirements.txt
