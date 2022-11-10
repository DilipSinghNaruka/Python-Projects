# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()


# import pyttsx3
# engine = pyttsx3.init()
# engine.say('Hello sir ')
# engine.say('Good morning')
# engine.runAndWait()




# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# rate = engine.getProperty('rate')
# engine.setProperty('voice', voices[1].id,)
# engine.setProperty( 'rate',rate+15)

# engine.say('Hello sir how are you ?')
# engine.runAndWait()
#


#import library

import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")