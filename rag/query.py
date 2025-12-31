from llama_index.core import VectorStoreIndex
from rag.llm import get_llm

def get_query_engine(index):
    return index.as_query_engine(
        similarity_top_k=5,
        llm=get_llm()
    )
