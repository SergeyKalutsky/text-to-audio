import json
import time
from tqdm import tqdm
from gtts import gTTS
from itertools import chain
from nltk.tokenize import word_tokenize
  


with open('corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)


i = 0
for word, translation in tqdm(corpus.items()):
    i += 1
    gTTS(text=word, lang='en', slow=False).save(f"audio/{word}.mp3")
    i += 1
    gTTS(text=corpus[word], lang='vi', slow=False).save(f"audio/{word}_t.mp3")
    time.sleep(0.5)

