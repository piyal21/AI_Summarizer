from typing import Dict, List
import chromadb
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

class VectorStore:
    def __init__(self, persist_directory: str = "chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection("pdf_documents")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def add_documents(self, documents: Dict[str, str]):
        """
        Add documents to the vector store.
        
        Args:
            documents: Dictionary with filename as key and text content as value
        """
        # Process in batches to avoid memory issues with large documents
        batch_size = 10
        filenames = list(documents.keys())
        texts = list(documents.values())
        
        for i in tqdm(range(0, len(filenames), batch_size), desc="Adding to vector store"):
            batch_files = filenames[i:i + batch_size]
            batch_texts = texts[i:i + batch_size]
            
            # Generate embeddings for the batch
            embeddings = self.model.encode(batch_texts)
            
            # Add to ChromaDB
            self.collection.add(
                documents=batch_texts,
                metadatas=[{"source": f} for f in batch_files],
                ids=[f"doc_{i + idx}" for idx in range(len(batch_files))],
                embeddings=embeddings.tolist()
            )

    def search(self, query: str, n_results: int = 5) -> List[Dict]:
        """
        Search for similar documents.
        
        Args:
            query: The search query
            n_results: Number of results to return
            
        Returns:
            List of dictionaries containing the results
        """
        # Generate embedding for the query
        query_embedding = self.model.encode(query)
        
        # Search in ChromaDB
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )
        
        # Format results
        formatted_results = []
        for idx in range(len(results['documents'][0])):
            formatted_results.append({
                'document': results['documents'][0][idx],
                'source': results['metadatas'][0][idx]['source'],
                'similarity': 1 - results['distances'][0][idx]  # Convert distance to similarity
            })
            
        return formatted_results