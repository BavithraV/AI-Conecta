import requests
from app.utils.azure_secrets import get_secret
from app.config.settings import settings

def translate(text: str, lang="es"):
    key = get_secret("AZURE_TRANSLATOR_KEY")

    url = f"{get_secret("AZURE_TRANSLATOR_ENDPOINT")}/translate?api-version=3.0&to={lang}"

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/json"
    }

    body = [{"text": text}]

    res = requests.post(url, headers=headers, json=body)

    return res.json()[0]["translations"][0]["text"]