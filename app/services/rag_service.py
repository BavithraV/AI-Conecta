from app.services.search_service import retrieve_documents
from app.utils.llm_client import generate_response
from app.utils.prompts import build_rag_prompt


def generate_answer(query: str):
    docs = retrieve_documents(query)

    context = "\n".join(docs)

    prompt = build_rag_prompt(context, query)

    return generate_response(prompt)
