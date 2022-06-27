from credentials import IAM_TOKEN, folder_id
import requests
# vi-en — вьетнамский-английский


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
