from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import StorageContext, VectorStoreIndex

from config.settings import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME
from ingest.embeddings import get_embedding_model
from rag.query import get_query_engine

# ---- SINGLETONS ----
_qdrant_client = None
_index = None
_query_engine = None


def get_query_engine_singleton():
    global _qdrant_client, _index, _query_engine

    if _query_engine is not None:
        return _query_engine

    _qdrant_client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY
    )

    vector_store = QdrantVectorStore(
        client=_qdrant_client,
        collection_name=COLLECTION_NAME
    )

    embed_model = get_embedding_model()

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    _index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        storage_context=storage_context,
        embed_model=embed_model
    )

    _query_engine = get_query_engine(_index)

    return _query_engine
