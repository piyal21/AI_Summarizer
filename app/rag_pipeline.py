from app.utils.text_splitter import split_text
from app.utils.vector_store import create_vector_db, retrieve_relevant
from app.config import OPENAI_API_KEY
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

def answer_query(doc_text, query, db_name="default_db"):
    chunks = split_text(doc_text)
    create_vector_db(chunks, db_name)
    relevant_chunks = retrieve_relevant(chunks, query, db_name)
    context = "\n".join(relevant_chunks)
    prompt = f"Based on the following document context, answer the user's question.\nContext:\n{context}\nQuestion: {query}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
