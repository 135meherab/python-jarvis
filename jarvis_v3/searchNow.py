import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

jarvis = pyttsx3.init("sapi5")
voices = jarvis.getProperty("voices")
jarvis.setProperty('voice',voices[0].id)
jarvis.setProperty('rate',170)

def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()

def takeCommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        listener.pause_threshold = 1
        listener.energy_threshold = 300
        voice = listener.listen(source,0,7)
    try:
        print("Recongnising.....")
        command = listener.recognize_google(voice,language='en-BD')
        print("Your command: "+ command)
    except Exception as e:
        return "None"
    return command

    command= takeCommand().lower()


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