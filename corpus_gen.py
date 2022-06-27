import json
from tqdm import tqdm
from translate import get_translation
from nltk.tokenize import word_tokenize


path = 'stories/p1.txt'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

d = {}
words = list(set(word_tokenize(text.lower())))
for i in tqdm(range(1, 15)):
    translate = words[i*500: i*500+500]
    translated = get_translation(translate, 'en', 'vi')
    assert len(translated) == len(translate)
    for word, word_t in zip(translate, translated):
        d[word] = word_t

with open('corpus.json', 'w') as f:
    json.dump(d, f)