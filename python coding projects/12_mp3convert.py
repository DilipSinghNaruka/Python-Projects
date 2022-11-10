# import os
from gtts import gTTS
# from playsound import playsound

my_text = "jai shree ram "
language = 'hi'
obj=gTTS(text = my_text,lang=language,slow=False)
obj.save('jaishreeram.mp3')      #save ka meaning jo mp3 file create hoee hai uuse save krna 
# playsound("E:\\my projects\\coding projects\\python\\python coding projects")
# obj.system('jaishreeram.mp3')

