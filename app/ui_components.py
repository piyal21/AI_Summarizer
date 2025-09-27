import streamlit as st

def render_upload():
    st.markdown("<div style='background-color:#f7f7f7;padding:20px;border-radius:10px;'>" \
                "<h3 style='color:#34495e;'>Upload Your Legal Document (PDF/DOC)</h3></div>", unsafe_allow_html=True)
    return st.file_uploader("Choose a file", type=["pdf", "doc", "docx"], label_visibility="collapsed")

def render_summary(summary):
    st.markdown("<div style='background-color:#eafaf1;padding:15px;border-radius:8px;'>" \
                f"<h4 style='color:#16a085;'>Summary</h4><p>{summary}</p></div>", unsafe_allow_html=True)

def render_highlights(highlights):
    st.markdown("<div style='background-color:#f9ebea;padding:15px;border-radius:8px;'>" \
                f"<h4 style='color:#c0392b;'>Key Topics & Highlights</h4><ul>{highlights}</ul></div>", unsafe_allow_html=True)

def render_chat(user_query, answer):
    st.markdown(f"<div style='background-color:#f4f6f7;padding:10px;border-radius:6px;margin-bottom:10px;'>" \
                f"<b>You:</b> {user_query}<br><b>AI:</b> {answer}</div>", unsafe_allow_html=True)
