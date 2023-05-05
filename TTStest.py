import rude
from gtts import gTTS
import random
from playsound import playsound
import os

while True:
    mytext = rude.insult()
# Language in which you want to convert
    language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
    myobj.save("insult.mp3")
  
# Playing the converted file
    playsound("welcome.mp3")
    os.remove("welcome.mp3")