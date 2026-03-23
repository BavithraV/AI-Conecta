from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

from app.utils.azure_secrets import get_secret
from app.config.settings import settings

def get_client():
    return SearchClient(
        endpoint=settings.AZURE_SEARCH_ENDPOINT,
        index_name=settings.AZURE_SEARCH_INDEX,
        credential=AzureKeyCredential(get_secret("AZURE_SEARCH_KEY"))
    )

def retrieve_documents(query: str):
    client = get_client()

    results = client.search(search_text=query, top=5)

    return [doc["content"] for doc in results]