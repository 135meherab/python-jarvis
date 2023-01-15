import pyttsx3

jarvis = pyttsx3.init('sapi5') # initialising desktop voices
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice',voices[0].id) # setup 0 index voice for jarvis
jarvis.setProperty('rate',170) # setup jarvis to speak slowly

# speak function to say string
def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()
