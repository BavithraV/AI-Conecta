import psycopg2
from app.utils.azure_secrets import get_secret


def get_connection():
    return psycopg2.connect(get_secret("POSTGRES_CONN"))
