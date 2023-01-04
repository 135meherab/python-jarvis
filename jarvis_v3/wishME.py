import pyttsx3
import datetime
jarvis = pyttsx3.init("sapi5")
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice',voices[0].id)
jarvis.setProperty("rate",170)

def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning, Sir!")
    elif hour>12 and hour<=18:
        speak("Good afternoon, Sir!")
    else:
        speak("Good evening, Sir!")
    speak("jarvis is always here for you, sir. How can I help you?")


