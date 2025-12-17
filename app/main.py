import streamlit as st
from app.config import OPENAI_API_KEY
from app.utils.file_handler import handle_upload
from app.utils.summarizer import generate_summary
from app.utils.highlight import extract_highlights
from app.rag_pipeline import answer_query
from app.chat_manager import get_chat_history, add_chat_history
from app.ui_components import render_upload, render_summary, render_chat, render_highlights
from app.utils.text_splitter import split_text
from app.utils.vector_store import create_vector_db

st.set_page_config(page_title="Legal AI Summarizer", layout="wide")
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>Legal AI Summarizer</h1>", unsafe_allow_html=True)

# Initialize session state
if 'doc_text' not in st.session_state:
    st.session_state.doc_text = None
if 'summary' not in st.session_state:
    st.session_state.summary = None
if 'highlights' not in st.session_state:
    st.session_state.highlights = None
if 'vector_db' not in st.session_state:
    st.session_state.vector_db = None
if 'processed_file' not in st.session_state:
    st.session_state.processed_file = None

uploaded_file = render_upload()

if uploaded_file:
    # Only process if it's a new file
    if st.session_state.processed_file != uploaded_file.name:
        try:
            with st.spinner("Processing document..."):
                # Extract text from document
                doc_text = handle_upload(uploaded_file)
                st.session_state.doc_text = doc_text

                # Generate summary
                summary = generate_summary(doc_text)
                st.session_state.summary = summary

                # Extract highlights
                highlights = extract_highlights(doc_text)
                st.session_state.highlights = highlights

                # Create vector DB for RAG
                chunks = split_text(doc_text)
                vector_db = create_vector_db(chunks, f"doc_{uploaded_file.name}")
                st.session_state.vector_db = vector_db

                st.session_state.processed_file = uploaded_file.name
                st.success("Document processed successfully!")
        except Exception as e:
            st.error(f"Error processing document: {str(e)}")

    # Display summary and highlights if available
    if st.session_state.summary:
        render_summary(st.session_state.summary)
    if st.session_state.highlights:
        render_highlights(st.session_state.highlights)

    # Chat interface
    st.markdown("---")
    st.subheader("Ask Questions About Your Document")

    # Display chat history
    chat_history = get_chat_history()
    if chat_history:
        st.markdown("### Previous Questions")
        for user_q, ai_ans in reversed(chat_history):
            render_chat(user_q, ai_ans)

    # Input for new question
    user_query = st.text_input("Type your question...", key="user_query_input")
    if user_query:
        try:
            with st.spinner("Generating answer..."):
                answer = answer_query(
                    st.session_state.doc_text,
                    user_query,
                    vector_db=st.session_state.vector_db
                )
                add_chat_history(user_query, answer)
                # Force rerun to show updated chat history
                st.rerun()
        except Exception as e:
            st.error(f"Error generating answer: {str(e)}")
else:
    st.info("Upload a PDF or DOC file to get started.")
