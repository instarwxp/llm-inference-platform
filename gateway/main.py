from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
import httpx
import time

app = FastAPI(title="LLM Inference Gateway", version="0.1.0")

Instrumentator().instrument(app).expose(app)

OLLAMA_BASE_URL = "http://192.168.32.1:11434"

class ChatRequest(BaseModel):
    model: str = "llama3.2"
    message: str
    stream: bool = False

class ChatResponse(BaseModel):
    model: str
    response: str
    latency_ms: float

@app.get("/health")
async def health():
    return {"status": "ok", "gateway": "llm-inference-platform"}

@app.get("/api/models")
async def list_models():
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
            return resp.json()
        except Exception as e:
            raise HTTPException(status_code=503, detail=f"Ollama unreachable: {str(e)}")

@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    start = time.time()
    async with httpx.AsyncClient(timeout=120) as client:
        try:
            resp = await client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": req.model,
                    "prompt": req.message,
                    "stream": False
                }
            )
            data = resp.json()
            latency = round((time.time() - start) * 1000, 2)
            return ChatResponse(
                model=req.model,
                response=data.get("response", ""),
                latency_ms=latency
            )
        except Exception as e:
            raise HTTPException(status_code=503, detail=str(e))
