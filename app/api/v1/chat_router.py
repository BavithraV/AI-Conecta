from fastapi import APIRouter
from app.services.rag_service import generate_answer

router = APIRouter()


@router.get("/chat")
def chat(query: str):
    return {"response": generate_answer(query)}
