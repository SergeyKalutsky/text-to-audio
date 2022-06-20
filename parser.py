import json
from itertools import chain
from random import sample

with open('Viet22K.txt', 'r', encoding='utf-8') as f:
    viet_words = f.readlines()

viet_words = [word.strip() for word in viet_words]

path = 'stories/p1.txt'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

paragraps = [t.replace('"', '') for t in text.split('\n') if t != '']

d = {}
for i, paragraph in enumerate(paragraps):
    text = [val.split(',') for val in paragraph.split('.')]
    texts = [i.strip() for i in chain(*text) if i != '']
    add = []

    for word in viet_words:
        if len(word) >= 3:
            for sentence in texts:
                if word in sentence:
                    add.append(word)

    sep_words = list(set(add))
    sep_words = sample(list(set(add)), int(0.2*len(sep_words)))
    d[i] = {}
    d[i]['paragraph'] = paragraph
    d[i]['sentences'] = texts
    d[i]['words'] = sep_words

with open('parsed.json', 'w', encoding='utf-8') as f:
     json.dump(d, f)