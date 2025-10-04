import pytest
from app.utils.file_handler import handle_upload
from pathlib import Path
import os

def test_handle_upload_pdf(tmp_path):
    # Create a mock PDF file
    pdf_content = b"%PDF-1.4\n%test pdf content"
    pdf_path = tmp_path / "test.pdf"
    pdf_path.write_bytes(pdf_content)
    
    # Test PDF handling
    with open(pdf_path, 'rb') as f:
        text = handle_upload(f)
    assert isinstance(text, str)

def test_handle_upload_doc(tmp_path):
    # Create a mock DOC file
    doc_content = b"Test document content"
    doc_path = tmp_path / "test.doc"
    doc_path.write_bytes(doc_content)
    
    # Test DOC handling
    with open(doc_path, 'rb') as f:
        text = handle_upload(f)
    assert isinstance(text, str)

def test_handle_upload_invalid():
    # Test invalid file handling
    with pytest.raises(ValueError):
        handle_upload(None)