# scripts/dev_query.py
from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import StorageContext, VectorStoreIndex

from config.settings import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME
from ingest.embeddings import get_embedding_model
from rag.query import get_query_engine

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

vector_store = QdrantVectorStore(
    client=client,
    collection_name=COLLECTION_NAME
)

embed_model = get_embedding_model()

storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store,
    storage_context=storage_context,
    embed_model=embed_model,
)

qe = get_query_engine(index)

response = qe.query(
    "Add your test question here"
)

print("\nANSWER:\n", response.response) # type: ignore
print("\nSOURCES:\n", response.get_formatted_sources())
