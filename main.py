import os
from src.pdf_processor import PDFProcessor
from src.vector_store import VectorStore
from dotenv import load_dotenv

def main():
    # Load environment variables if needed
    load_dotenv()

    # Initialize processors
    pdf_dir = "PDF Files"  # Directory containing PDF files
    vector_db_dir = "chroma_db"  # Directory to store vector database
    
    # Create PDF processor
    pdf_processor = PDFProcessor(pdf_dir)
    
    # Process all PDFs
    print("Processing PDF files...")
    documents = pdf_processor.process_all_pdfs()
    
    if not documents:
        print("No PDF files found or processed.")
        return
    
    print(f"Successfully processed {len(documents)} PDF files.")
    
    # Initialize vector store
    print("Initializing vector store...")
    vector_store = VectorStore(persist_directory=vector_db_dir)
    
    # Add documents to vector store
    print("Adding documents to vector store...")
    vector_store.add_documents(documents)
    
    print("Process completed successfully!")
    
    # Example search (uncomment to test)
    # query = "your search query here"
    # results = vector_store.search(query, n_results=3)
    # for result in results:
    #     print(f"Document: {result['source']}")
    #     print(f"Similarity: {result['similarity']:.2f}")
    #     print(f"Content snippet: {result['document'][:200]}...")
    #     print("-" * 80)

if __name__ == "__main__":
    main()