import datetime
import mediaControl
import opneCloseWeb
import pyttsx3
import speech_recognition as sr

import reminder
import searchNow

jarvis = pyttsx3.init('sapi5') # initialising desktop voices
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice',voices[0].id) # setup 0 index voice for jarvis
jarvis.setProperty('rate',170) # setup jarvis to speak slowly

# speak function to say string
def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()

# taking voice with microphone
def takeCommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        listener.pause_threshold = 1
        listener.energy_threshold = 300
        voice = listener.listen(source,0,7)
    try:
        print("recognizing.....")
        command = listener.recognize_google(voice,language='en-BD')
        print("Your command:" + command)
    except Exception as e:
        return 'None'
    return command

if __name__ == '__main__':
    while True:
        command = takeCommand().lower()
        if "are you there" in command or "hey jarvis" in command or "wake up" in command:
            from wishME import wishme
            wishme()

            while True:
                command= takeCommand().lower()
                if "stop" in command:
                    speak("ok,sir! you can call me any time.")
                    break
                elif "open" in command:
                    opneCloseWeb.openwebapp(command)
                elif "close" in command:
                    opneCloseWeb.closewebapp(command)
                elif "search for" in command:
                    searchNow.searching(command)
                elif "tell me about" in command:
                    searchNow.wikisearch(command)
                elif "on youtube" in command:
                    searchNow.youtubesearch(command)
                elif "pause" in command:
                    speak("paused the video")
                    mediaControl.pause(command)
                elif "play" in command:
                    speak("playing the video")
                    mediaControl.play(command)
                elif "mute" in command:
                    speak("muted")
                    mediaControl.mute()
                elif "unmute" in command:
                    speak("unmuted")
                    mediaControl.unmute()
                elif "volume up" in command:
                    mediaControl.volumeup()
                    speak("turning volume up")
                elif "volume down" in command:
                    mediaControl.volumedown()
                    speak("turning volume down")
                elif "remember that" in command:
                    reminder.reminder_msg(command)
                elif 'what is the schedule' in command:
                    remember = open("remember.txt","r")
                    speak(remember.read())
                elif "time" in command:
                    strtime = datetime.datetime.now().strftime("%I:%M %p")
                    speak(f"Current time is {strtime}")
                elif "shutdown" in command or "shut down" in command:
                    print("shutting down the full program")
                    speak("shutting down the full program")
                    exit()
                else:
                    print("I can't recognize your command. please say that again")
                    speak("I can't recognize your command. please say that again")





