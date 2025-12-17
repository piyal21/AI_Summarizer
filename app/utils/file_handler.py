import os
import PyPDF2
from docx import Document

def handle_upload(uploaded_file):
    """
    Extract text from uploaded PDF or DOCX file.

    Args:
        uploaded_file: Streamlit uploaded file object

    Returns:
        str: Extracted text from the document

    Raises:
        ValueError: If file type is not supported
        Exception: If file parsing fails
    """
    try:
        ext = uploaded_file.name.split('.')[-1].lower()

        if ext == 'pdf':
            reader = PyPDF2.PdfReader(uploaded_file)
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

            if not text.strip():
                raise ValueError("PDF file appears to be empty or contains no extractable text")

        elif ext in ['doc', 'docx']:
            doc = Document(uploaded_file)
            text = "\n".join([para.text for para in doc.paragraphs])

            if not text.strip():
                raise ValueError("Document appears to be empty")

        else:
            raise ValueError(f"Unsupported file type: .{ext}. Please upload a PDF or DOCX file.")

        return text

    except ValueError:
        raise
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")
