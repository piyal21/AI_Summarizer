import pytest
import os
from app.utils.summarizer import generate_summary
from app.utils.highlight import extract_highlights

def test_generate_summary():
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OpenAI API key not found")
    
    test_text = """
    This is a legal document that contains important information.
    The party of the first part hereby agrees to the terms.
    The deadline for submission is December 31, 2025.
    """
    summary = generate_summary(test_text)
    assert isinstance(summary, str)
    assert len(summary) > 0

def test_extract_highlights():
    test_text = """
    IMPORTANT: All submissions must be made by December 31, 2025.
    WARNING: Failure to comply may result in penalties.
    NOTE: Please read all terms carefully before signing.
    """
    highlights = extract_highlights(test_text)
    assert isinstance(highlights, list)
    assert len(highlights) > 0
    for highlight in highlights:
        assert isinstance(highlight, str)