import rude
from gtts import gTTS
import random
from playsound import playsound
import os


def tts(num):
    os.system('rm -r saving')
    os.mkdir('saving')
    ttsnum = 0
    for i in range(num):
        ttsnum += 1
        mytext = rude.insult()
        os.chdir('saving')
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        filename = str(ttsnum) + '.mp3'
        myobj.save(filename)
        print(filename)
        os.chdir('..')