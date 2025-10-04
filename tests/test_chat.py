import pytest
import os
from app.rag_pipeline import answer_query
from app.chat_manager import get_chat_history, add_chat_history

def test_answer_query():
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OpenAI API key not found")
        
    test_doc = "This is a test document about legal terms. The deadline is December 31."
    query = "What is the deadline?"
    answer = answer_query(test_doc, query)
    assert isinstance(answer, str)
    assert len(answer) > 0

def test_chat_history():
    # Test adding to chat history
    query = "Test question"
    answer = "Test answer"
    add_chat_history(query, answer)
    
    # Test retrieving chat history
    history = get_chat_history()
    assert isinstance(history, list)
    assert len(history) > 0
    
    # Check the latest chat entry
    latest = history[-1]
    assert latest["query"] == query
    assert latest["answer"] == answer