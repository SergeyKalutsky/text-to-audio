import requests
# vi-en — вьетнамский-английский

IAM_TOKEN = 't1.9euelZqVm8mak5iNncqUk4qWmsmRju3rnpWak82Rx8qJmJeQzo-Tj8eUkI7l9PdpHD5q-e9cIQSW3fT3KUs7avnvXCEElg.SUwJqHYVJR3wCJcVKJFKdoq8RltqdlU0tVAaQSjd-q1F69YgLAqk6VQWugXEda-mWmns5z-H3vLdd9-7AxESCQ'
folder_id = 'b1goa1c00ojbbe6nqbmr'
target_language = 'ru'
source_language = 'vi'

# body = {
#     "sourceLanguageCode": source_language,
#     "targetLanguageCode": target_language,
#     "texts": texts,
#     "folderId": folder_id,
# }

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {IAM_TOKEN}"
# }

# response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
#     json = body,
#     headers = headers
# )

# print(response.text)