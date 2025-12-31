from fastapi import FastAPI, HTTPException
from api.schemas import QueryRequest, QueryResponse
from api.dependencies import get_query_engine_singleton

app = FastAPI(
    title="Costa Rica Election RAG API",
    description="Ask questions about election plans",
    version="0.1.0"
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query_rag(payload: QueryRequest):
    try:
        qe = get_query_engine_singleton()
        response = qe.query(payload.question)

        return QueryResponse(
            answer=response.response, # type: ignore
            sources=response.get_formatted_sources()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    