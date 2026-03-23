from openai import AzureOpenAI
from app.utils.azure_secrets import get_secret
from app.config.settings import settings

def get_client():
    return AzureOpenAI(
        api_key=get_secret("AZURE_OPENAI_KEY"),
        api_version=settings.AZURE_OPENAI_API_VERSION,
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
    )

def generate_response(prompt: str):
    client = get_client()

    res = client.chat.completions.create(
        model=settings.AZURE_OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content