from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.v1.chat_router import router as chat_router
from app.api.v1.upload_router import router as upload_router
from app.core.monitoring import setup_monitoring

load_dotenv()

app = FastAPI(title="AI-Conecta RAG API")

setup_monitoring()

app.include_router(chat_router, prefix="/api/v1")
app.include_router(upload_router, prefix="/api/v1")

@app.get("/")
def health():
    return {"status": "running"}