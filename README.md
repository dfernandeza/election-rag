# 🗳️ Election RAG — Open-Source Retrieval-Augmented QA with Qdrant

An end-to-end **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions about political party election plans and receive **grounded, source-backed answers**.

This project uses:

- [**Qdrant Cloud**](https://qdrant.tech/cloud/) as the vector database
- **Local embeddings** (HuggingFace / Sentence Transformers)
- **Local LLM** via Ollama (no paid APIs)
- **FastAPI** as a production-ready backend
- **Zero paid APIs**

Designed as a **realistic, minimal, and well-structured RAG system**, suitable for educational use, civic transparency, and as a reference architecture.

---

## ✨ Features

- 📄 Ingests multiple PDF documents (party programs, manifestos, plans)
- 🔍 Semantic search using vector embeddings
- 🧠 Grounded answers using RAG (no fine-tuning)
- 🔗 Source citations for every answer
- ☁️ Uses [**Qdrant Cloud**](https://qdrant.tech/cloud/) (free tier supported)
- 🧠 Fully local inference (zero OpenAI / paid LLM APIs)
- 🚀 FastAPI service
- 🧱 Clean, modular Python architecture

---

## 🧠 Architecture Overview

```
PDFs
↓
Text Extraction
↓
Chunking (512 tokens)
↓
Local Embeddings (Sentence Transformers)
↓
Qdrant Cloud (Vector Storage)
↓
Retriever (Top-K similarity search)
↓
Local LLM (Ollama)
↓
FastAPI (/query endpoint)
```

---

## 🧰 Tech Stack

| Component     | Technology                        |
| ------------- | --------------------------------- |
| Vector DB     | Qdrant Cloud                      |
| Embeddings    | HuggingFace (`bge-small-en-v1.5`) |
| LLM           | Ollama (`llama3`)                 |
| RAG Framework | LlamaIndex                        |
| API           | FastAPI                           |
| PDF Parsing   | PyPDF                             |
| Language      | Python 3.10+                      |

---

## 📁 Project Structure

```
election-rag/
├── api/                # FastAPI app
├── ingest/             # PDF ingestion & indexing
├── rag/                # Query & LLM logic
├── config/             # Environment-based settings
├── data/
│   └── raw/pdfs/       # Input PDFs
├── scripts/            # Dev & testing scripts
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

- Python **3.10+**
- Ollama (for local LLM)
- A [Qdrant Cloud account](https://qdrant.tech/cloud/) (free tier)

---

### 2️⃣ Install Ollama (local LLM)

```bash
brew install ollama
ollama serve
ollama pull llama3
```

Verify:

```bash
ollama run llama3 "Hello"
```

### 3️⃣ Clone the repository

```bash
git clone https://github.com/your-username/election-rag.git
cd election-rag
```

### 4️⃣ Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 5️⃣ Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Or manually:

```bash
pip install \
  fastapi uvicorn \
  llama-index \
  llama-index-llms-ollama \
  llama-index-embeddings-huggingface \
  llama-index-vector-stores-qdrant \
  qdrant-client \
  sentence-transformers \
  pypdf \
  python-dotenv
```

## ☁️ Qdrant Cloud Setup

1. Create a free Qdrant Cloud cluster
2. Copy:
   - Cluster URL
   - API key

Create a .env file:

```env
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your_api_key_here
```

## 📄 Add Your PDFs

Place election plans here:

`data/raw/pdfs/`

## 🧱 Ingest Documents (One-Time Step)

This:
• Loads PDFs
• Chunks text
• Generates embeddings
• Stores vectors in Qdrant Cloud

```bash
python -m ingest.run_ingest
```

## 🧪 Local Query Test (Optional)

```bash
python -m scripts.dev_query
```

## 🌐 Run the API

```bash
uvicorn api.app:app --reload
```

Server runs at: `http://127.0.0.1:8000`

## 📘 API Usage

### Ask a Question

```
POST /query
Content-Type: application/json
```

### Body

```json
{
  "question": "What does Party A propose about healthcare?"
}
```

### Sample Response

```json
{
  "answer": "Party A proposes increasing healthcare funding...",
  "sources": "party_a_2025.pdf (page 12)"
}
```

## ⚠️ Notes on Accuracy & Safety

- Answers are grounded in retrieved documents
- Local LLMs may hallucinate — always verify sources
- Intended for educational and informational use
