import json
from tqdm import tqdm
from gtts import gTTS
  

# with open('parsed_translated.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# sentences = data['0']['sentences']
# sentences_translated = data['0']['sentences_translated']
sentence = 'No one would have believed in the last years of the nineteenth century that this world was being watched keenly and closely by intelligences greater than man’s and yet as mortal as his own; that as men busied themselves about their various concerns they were scrutinised and studied, perhaps almost as narrowly as a man with a microscope might scrutinise the transient creatures that swarm and multiply in a drop of water. With infinite complacency men went to and fro over this globe about their little affairs, serene in their assurance of their empire over matter. It is possible that the infusoria under the microscope do the same. No one gave a thought to the older worlds of space as sources of human danger, or thought of them only to dismiss the idea of life upon them as impossible or improbable. It is curious to recall some of the mental habits of those departed days. At most terrestrial men fancied there might be other men upon Mars, perhaps inferior to themselves and ready to welcome a missionary enterprise. Yet across the gulf of space, minds that are to our minds as ours are to those of the beasts that perish, intellects vast and cool and unsympathetic, regarded this earth with envious eyes, and slowly and surely drew their plans against us. And early in the twentieth century came the great disillusionment.'
gTTS(text=sentence, lang='en', slow=False).save(f"audio.mp3")

# for key in tqdm(data):
#     for sent, setn_t in zip(data[key]['sentences'], data[key]['sentences_translated']):
#         myobj = gTTS(text=sent, lang='vi', slow=False).save(f"audio/{i}.mp3")
#         i += 1
#         myobj = gTTS(text=setn_t, lang='ru', slow=False).save(f"audio/{i}.mp3")
#         i += 1
#     for word, word_t in zip(data[key]['words'], data[key]['words_translated']):
#         myobj = gTTS(text=word, lang='vi', slow=False).save(f"audio/{i}.mp3")
#         i += 1
#         myobj = gTTS(text=word_t, lang='ru', slow=False).save(f"audio/{i}.mp3")
#         i += 1
#     myobj = gTTS(text=data[key]['paragraph'], lang='vi', slow=False)
    
