import os
from langchain_community.vectorstores import FAISS, Chroma
from langchain_openai import OpenAIEmbeddings
from app.config import OPENAI_API_KEY, VECTOR_DB_PATH

embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

# Use FAISS by default
VECTOR_DB_TYPE = 'faiss'

def create_vector_db(chunks, db_name):
    if VECTOR_DB_TYPE == 'faiss':
        db = FAISS.from_texts(chunks, embeddings)
        db.save_local(os.path.join(VECTOR_DB_PATH, db_name))
    else:
        db = Chroma.from_texts(chunks, embeddings, persist_directory=os.path.join(VECTOR_DB_PATH, db_name))
    return db

def load_vector_db(db_name):
    if VECTOR_DB_TYPE == 'faiss':
        return FAISS.load_local(os.path.join(VECTOR_DB_PATH, db_name), embeddings, allow_dangerous_deserialization=True)
    else:
        return Chroma(persist_directory=os.path.join(VECTOR_DB_PATH, db_name), embedding_function=embeddings)

def retrieve_relevant(chunks, query, db_name):
    db = load_vector_db(db_name)
    docs = db.similarity_search(query, k=5)
    return [doc.page_content for doc in docs]
