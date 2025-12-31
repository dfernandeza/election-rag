from ingest.loaders import load_pdfs
from ingest.chunking import chunk_documents
from ingest.embeddings import get_embedding_model
from ingest.index import build_index

PDF_PATH = "data/raw/pdfs"

def main():
    print("Loading PDFs...")
    docs = load_pdfs(PDF_PATH)

    print("Chunking...")
    nodes = chunk_documents(docs)

    print(f"Chunks created: {len(nodes)}")

    print("Embedding & indexing...")
    embed_model = get_embedding_model()
    build_index(nodes, embed_model)

    print("Ingestion complete ✅")

if __name__ == "__main__":
    main()
