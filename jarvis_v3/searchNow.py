import speech_recognition as sr
import pywhatkit
import wikipedia

from speak import speak
from takeCommand import takeCommand


def searching(command):
    if 'search for' in command:
        command = command.replace('jarvis','')
        command = command.replace('search for','')
        try:
            print("Searching on google for" + command)
            speak("Searching on google for" + command)
            pywhatkit.search(command)

        except:
            print("sorry sir! I did not find any result!")
            speak("sorry sir! I did not find any result!")


def youtubesearch(command):
    if "play" and "on youtube" in command:
        command = command.replace('play','')
        command = command.replace('on youtube','')
        command = command.replace('jarvis','')
        try:
            print("playing "+ command)
            speak("playing" + command)
            pywhatkit.playonyt(command)

        except:
            print("sorry sir! I did not find any result!")
            speak("sorry sir! I did not find any result!")


def wikisearch(command):
    if 'tell me about' in command:
        command = command.replace('tell me about','')
        command = command.replace('jarvis','')
        speak("Searching on Wikipedia......")
        try:
            information=wikipedia.summary(command,2)
            print(information)
            speak(information)
        except:
            print("sorry sir! I did not find any result!")
            speak("sorry sir! I did not find any result!")