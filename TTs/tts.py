# Import the required module for text  
# to speech conversion 
from gtts import * 
  
# This module is imported so that we can  
# play the converted audio 
import os
import time 
  
  
def saveInMp3File(sentence):
    response = gTTS(text=sentence, lang='en', slow=False)
    d = str(time.time())
    
    response.save(d+ "-voice.mp3") 
 
saveInMp3File("Hello amit kumar prajapati"); 