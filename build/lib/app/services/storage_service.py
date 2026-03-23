from azure.storage.blob import BlobServiceClient
from app.utils.azure_secrets import get_secret
from app.config.settings import settings

def upload_file(filename: str, data: bytes):
    client = BlobServiceClient.from_connection_string(
        get_secret("AZURE_STORAGE_CONNECTION_STRING")
    )

    blob = client.get_blob_client(
        container=settings.AZURE_STORAGE_CONTAINER,
        blob=filename
    )

    blob.upload_blob(data, overwrite=True)