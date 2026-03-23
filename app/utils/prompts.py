def build_rag_prompt(context: str, query: str):
    return f"""
    Answer ONLY using the given context.

    Context:
    {context}

    Question:
    {query}
    """
