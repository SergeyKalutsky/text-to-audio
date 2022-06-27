import json
from tqdm import tqdm
from gtts import gTTS
from itertools import chain
from nltk.tokenize import word_tokenize
  


common_words = ['she', 'he', 'can', 'the', 'a', 'of', 'and', 'as', 
'that', 'this', 'was', 'is', 'in', 'at', 'on', 'no', 'yes', 'by', 'his', 'her', 'being', 'man',
'to', 'their', 'go', 'went', 'with', 'would', 'might', 'yet', 'were', 'are']
path = 'stories/p1.txt'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

with open('corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

sentenses = [val.strip() for val in chain(*[chunk.split('.') for chunk in text.split('\n')]) if val not in (' ', '')]
i = 0
for sentence in tqdm(sentenses):
    gTTS(text=sentence, lang='en', slow=False).save(f"audio/{i}.mp3")
    word_tokens = list(set(word_tokenize(sentence.lower())))
    word_tokens = [word for word in word_tokens if word not in common_words and len(word) > 1]
    for word in word_tokens:
        if word in corpus:
            i += 1
            gTTS(text=word, lang='en', slow=False).save(f"audio/{i}.mp3")
            i += 1
            gTTS(text=corpus[word], lang='vi', slow=False).save(f"audio/{i}.mp3")
