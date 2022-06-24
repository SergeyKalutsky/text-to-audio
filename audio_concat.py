from tqdm import tqdm
from pydub import AudioSegment

end_sound = AudioSegment.silent(duration=200) 
for i in tqdm(range(1154)):
    try:
        end_sound += AudioSegment.from_mp3(f"audio/{i}.mp3") + AudioSegment.silent(duration=1500) 
    except Exception as e:
        print(e)
end_sound.export("mashup.mp3", format="mp3")