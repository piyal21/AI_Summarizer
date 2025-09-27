import streamlit as st
from app.config import OPENAI_API_KEY
from app.utils.file_handler import handle_upload
from app.utils.summarizer import generate_summary
from app.utils.highlight import extract_highlights
from app.rag_pipeline import answer_query
from app.chat_manager import get_chat_history, add_chat_history
from app.ui_components import render_upload, render_summary, render_chat, render_highlights

st.set_page_config(page_title="Legal AI Summarizer", layout="wide")
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>Legal AI Summarizer</h1>", unsafe_allow_html=True)

uploaded_file = render_upload()

if uploaded_file:
    doc_text = handle_upload(uploaded_file)
    summary = generate_summary(doc_text)
    highlights = extract_highlights(doc_text)
    render_summary(summary)
    render_highlights(highlights)
    st.markdown("---")
    st.subheader("Ask Questions About Your Document")
    user_query = st.text_input("Type your question...")
    if user_query:
        answer = answer_query(doc_text, user_query)
        add_chat_history(user_query, answer)
        render_chat(user_query, answer)
else:
    st.info("Upload a PDF or DOC file to get started.")
