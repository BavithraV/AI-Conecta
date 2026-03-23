import os


class BaseConfig:
    ENV = os.getenv("ENV", "dev")

    AZURE_KEYVAULT_URL = os.getenv("AZURE_KEYVAULT_URL")

    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
