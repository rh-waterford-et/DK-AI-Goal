# RAG with LlamaStack

A complete Retrieval-Augmented Generation (RAG) system built with LlamaStack, demonstrating semantic search and AI-powered question answering.

## 🎯 What This Project Does

This project showcases a fully functional RAG system that:
- ✅ Connects to LlamaStack server with Ollama backend
- ✅ Creates vector databases for document storage
- ✅ Performs semantic search on documents
- ✅ Includes an AI agent for interactive Q&A
- ✅ Provides both notebook and script interfaces

## 🛠️ Prerequisites

### Required Services
1. **Ollama** running on port 11434 with `llama3.2:3b` model
2. **LlamaStack server** running on port 8321

### Installation
```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the required model
ollama pull llama3.2:3b

# Install project dependencies
uv sync
```

## 🚀 Quick Start

### 1. Start LlamaStack Server
```bash
INFERENCE_MODEL=llama3.2:3b uv run --with llama-stack llama stack build --template ollama --image-type venv --run
```

### 2. Run the Demo

**Option A: Jupyter Notebook (Interactive)**
```bash
uv run jupyter notebook
# Open app.ipynb and run all cells
```

**Option B: Python Script (Automated)**
```bash
uv run python test_rag.py
```

## 📁 Project Structure

```
AI-Goal/
├── app.ipynb              # 📓 Interactive Jupyter notebook demo
├── test_rag.py            # 🐍 Standalone Python script demo
├── pyproject.toml         # 📦 Project configuration
├── uv.lock               # 🔒 Dependency lock file
├── .python-version       # 🐍 Python version specification
└── README.md             # 📖 This file
```

## 🔧 How It Works

### 1. **Vector Database Creation**
- Uses Faiss for vector storage
- 384-dimensional embeddings via `all-MiniLM-L6-v2`
- Automatic document chunking and indexing

### 2. **Semantic Search**
- Converts queries to embeddings
- Finds semantically similar documents
- Returns ranked results with metadata

### 3. **RAG Agent (Optional)**
- Creates an AI agent with access to the knowledge base
- Uses `builtin::rag/knowledge_search` tool
- Provides conversational interface

## 📊 Example Usage

The system includes sample documents about:
- **RAG (Retrieval-Augmented Generation)** concepts
- **LlamaStack** platform overview  
- **Vector databases** and semantic search

### Sample Queries:
- "What is RAG?"
- "Tell me about LlamaStack"
- "How do vector databases work?"

## 🎛️ Configuration

### Environment Variables
- `LLAMA_STACK_PORT=8321` - LlamaStack server port

### Models Used
- **LLM**: `llama3.2:3b` (via Ollama)
- **Embeddings**: `all-MiniLM-L6-v2` (via LlamaStack)

## 🐛 Troubleshooting

### Common Issues

**Import Error: `llama_stack_client`**
```bash
# Make sure you're using the uv environment
uv run python your_script.py
# Or for Jupyter
uv run jupyter notebook
```

**Connection Error to LlamaStack**
- Ensure LlamaStack server is running on port 8321
- Check that Ollama is running with llama3.2:3b model

**Kernel Issues in Jupyter**
- Use the "AI Goal RAG Environment" kernel if available
- Or run: `uv run jupyter notebook` to use correct environment

## 📈 Features Demonstrated

- [x] **Vector Database Management** - Create, populate, query, cleanup
- [x] **Semantic Search** - Meaning-based document retrieval
- [x] **Error Handling** - Robust error handling and debugging
- [x] **Multiple Interfaces** - Both notebook and script versions
- [x] **AI Agent Integration** - Conversational RAG interface
- [x] **Production Ready** - Proper dependency management with uv

## 🤝 Contributing

This project demonstrates RAG concepts with LlamaStack. Feel free to:
- Add more document types
- Experiment with different embedding models
- Extend the AI agent capabilities
- Improve the user interface

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Related Links

- [LlamaStack Documentation](https://github.com/meta-llama/llama-stack)
- [Ollama](https://ollama.ai/)
- [Faiss Vector Database](https://github.com/facebookresearch/faiss) 