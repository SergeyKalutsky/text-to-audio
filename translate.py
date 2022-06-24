import time
import json
import requests
from tqdm import tqdm
# vi-en — вьетнамский-английский

IAM_TOKEN = 't1.9euelZqdicuPm5OWlJ2Mj8aZmsjMk-3rnpWak82Rx8qJmJeQzo-Tj8eUkI7l9PcrHClq-e86GHrw3fT3a0omavnvOhh68A.DFXqe9ZhfYgCmbMasH0kG5aojnRCuooZq0-SK1QbpNmB7WXB3FS7ooba5ROPYrXm6DWr0JDveCNZrTwgBGk0DQ'
folder_id = 'b1goa1c00ojbbe6nqbmr'

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {IAM_TOKEN}"
}


def get_translation(texts, source_lang, target_lang):

    body = {
        "sourceLanguageCode": source_lang,
        "targetLanguageCode": target_lang,
        "folderId": folder_id,
        "texts": texts
    }
    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers)
    res = response.json()
    if 'translations' in res:
        return [sentence['text'] for sentence in res['translations']]
    return []
    
