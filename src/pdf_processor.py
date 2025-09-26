from typing import List, Dict
import os
from PyPDF2 import PdfReader
from tqdm import tqdm

class PDFProcessor:
    def __init__(self, pdf_directory: str):
        self.pdf_directory = pdf_directory

    def get_pdf_files(self) -> List[str]:
        """Get all PDF files from the directory."""
        return [f for f in os.listdir(self.pdf_directory) 
                if f.lower().endswith('.pdf')]

    def extract_text(self, pdf_path: str) -> str:
        """Extract text from a single PDF file."""
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text.strip()
        except Exception as e:
            print(f"Error processing {pdf_path}: {str(e)}")
            return ""

    def process_all_pdfs(self) -> Dict[str, str]:
        """Process all PDFs in the directory and return a dictionary of filename: text."""
        pdf_files = self.get_pdf_files()
        results = {}
        
        for pdf_file in tqdm(pdf_files, desc="Processing PDFs"):
            full_path = os.path.join(self.pdf_directory, pdf_file)
            text = self.extract_text(full_path)
            if text:
                results[pdf_file] = text
        
        return results