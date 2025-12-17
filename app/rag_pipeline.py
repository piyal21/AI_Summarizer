from app.utils.text_splitter import split_text
from app.utils.vector_store import create_vector_db, retrieve_relevant, load_vector_db
from app.config import OPENAI_API_KEY
from openai import OpenAI
import os

client = OpenAI(api_key=OPENAI_API_KEY)

def answer_query(doc_text, query, db_name="default_db", vector_db=None):
    """
    Answer a query using RAG pipeline.
    If vector_db is provided, reuse it. Otherwise create a new one.
    """
    try:
        # If vector DB is not provided, create it
        if vector_db is None:
            chunks = split_text(doc_text)
            vector_db = create_vector_db(chunks, db_name)

        # Retrieve relevant chunks using the vector DB
        docs = vector_db.similarity_search(query, k=5)
        relevant_chunks = [doc.page_content for doc in docs]

        context = "\n".join(relevant_chunks)
        prompt = f"Based on the following document context, answer the user's question.\nContext:\n{context}\nQuestion: {query}"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error answering query: {str(e)}"
