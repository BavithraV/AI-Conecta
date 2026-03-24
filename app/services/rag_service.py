from app.services.search_service import retrieve_documents
from app.services.translator_service import translate
from app.utils.llm_client import generate_response

def rag_pipeline(query: str, lang="en"):
    docs = retrieve_documents(query)

    context = "\n".join(docs)

    if lang != "en":
        context = translate(context, lang)

    prompt = f"""
    Answer ONLY from context:

    {context}

    Question: {query}
    """

    return generate_response(prompt)
