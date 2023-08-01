from gtts import gTTS
import os
from playsound import playsound

#creates a audio file and plays it

def play_audio(text, file_name='std.mp3'):
    
    file = gTTS(text, lang='pt-br')
    file.save(os.path.join('alfreds_sounds', file_name))
    
    path = os.path.abspath(os.path.join('alfreds_sounds', file_name))
    
    playsound(path)
    
#creating tts .mp3 files and saving to 'alfreds_sounds'

talk = gTTS('Pode falar', lang='pt-br')
talk.save(os.path.join('alfreds_sounds', 'talk.mp3'))

error = gTTS('Fale novamente por favor', lang='pt-br')
error.save(os.path.join('alfreds_sounds', 'error.mp3'))