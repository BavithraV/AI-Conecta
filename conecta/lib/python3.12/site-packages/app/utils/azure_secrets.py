from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from app.config.settings import settings

_client = SecretClient(
    vault_url=settings.AZURE_KEYVAULT_URL,
    credential=DefaultAzureCredential()
)

def get_secret(name: str) -> str:
    return _client.get_secret(name).value