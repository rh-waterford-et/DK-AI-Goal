# RAG with LlamaStack - Test Script
import os
from llama_stack_client import LlamaStackClient
import uuid

# Set environment variable for this script
os.environ['LLAMA_STACK_PORT'] = '8321'

def test_rag_system():
    print("🧪 Testing RAG system...")
    
    # Check if environment variable is set
    if 'LLAMA_STACK_PORT' not in os.environ:
        print("❌ LLAMA_STACK_PORT environment variable not set!")
        return False
    else:
        print(f"✅ LLAMA_STACK_PORT set to {os.environ['LLAMA_STACK_PORT']}")

    # Create client
    client = LlamaStackClient(base_url=f"http://localhost:{os.environ['LLAMA_STACK_PORT']}")

    try:
        # Test connection first
        models = client.models.list()
        print(f"✅ Connected! Found {len(models)} models:")
        for model in models:
            print(f"  - {model.model_type}: {model.identifier}")
        
        # Register a vector database with unique ID
        vector_db_id = f"my_documents_{uuid.uuid4().hex[:8]}"
        print(f"\n📊 Creating vector database: {vector_db_id}")
        
        response = client.vector_dbs.register(
            vector_db_id=vector_db_id,
            embedding_model="all-MiniLM-L6-v2",
            embedding_dimension=384,
            provider_id="faiss",
        )
        print("✅ Vector DB registered successfully!")

        # Insert sample documents about AI and RAG
        chunks = [
            {
                "content": "Retrieval-Augmented Generation (RAG) is a technique that combines information retrieval with text generation. It allows language models to access external knowledge sources to provide more accurate and up-to-date responses.",
                "mime_type": "text/plain",
                "metadata": {
                    "document_id": "rag_intro",
                    "topic": "RAG basics",
                },
            },
            {
                "content": "LlamaStack is an open-source platform that provides standardized APIs for building AI applications. It supports various providers for inference, vector storage, and other AI capabilities.",
                "mime_type": "text/plain",
                "metadata": {
                    "document_id": "llamastack_info",
                    "topic": "LlamaStack overview",
                },
            },
            {
                "content": "Vector databases store high-dimensional embeddings that represent the semantic meaning of text. This enables semantic search and retrieval based on meaning rather than exact keyword matches.",
                "mime_type": "text/plain",
                "metadata": {
                    "document_id": "vector_db_info",
                    "topic": "Vector databases",
                },
            },
        ]
        
        print(f"\n📝 Inserting {len(chunks)} document chunks...")
        client.vector_io.insert(vector_db_id=vector_db_id, chunks=chunks)
        print("✅ Document chunks inserted successfully!")

        # Test queries
        test_queries = [
            "What is RAG?",
            "Tell me about LlamaStack",  
            "How do vector databases work?"
        ]
        
        print("\n🔍 Testing RAG queries:")
        for query in test_queries:
            print(f"\nQuery: '{query}'")
            chunks_response = client.vector_io.query(
                vector_db_id=vector_db_id, 
                query=query
            )
            print(f"Found {len(chunks_response.chunks)} relevant chunks:")
            for i, chunk in enumerate(chunks_response.chunks, 1):
                score = getattr(chunk, 'score', 0.0)
                print(f"  {i}. Score: {score:.3f}")
                print(f"     Content: {chunk.content[:100]}...")
        
        # Clean up
        print(f"\n🧹 Cleaning up vector database...")
        client.vector_dbs.unregister(vector_db_id)
        print("✅ Cleanup completed!")
        
        print("\n🎉 RAG system is working perfectly!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure LlamaStack server is running on port", os.environ.get('LLAMA_STACK_PORT', '8321'))
        return False

if __name__ == "__main__":
    success = test_rag_system()
    if success:
        print("\n✅ All tests passed! Your RAG system is ready.")
    else:
        print("\n❌ Tests failed. Please check your setup.") 