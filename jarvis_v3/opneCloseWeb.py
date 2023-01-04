import os
import pyautogui
import webbrowser
import pyttsx3

jarvis = pyttsx3.init("sapi5")
voices = jarvis.getProperty("voices")
jarvis.setProperty("voice",voices[0].id)
jarvis.setProperty("rate",170)


def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()



def openwebapp(command):
    speak("launching, sir.")
    if ".com" or ".gov" or ".bd" or ".org" or ".edu" in command:
        command = command.replace('open','')
        command = command.replace('jarvis', '')
        command = command.replace(' ','')
        webbrowser.open(f"https://{command}")



def closewebapp(command):
    speak("closing, sir")
    if "close the tab" in command:
        pyautogui.hotkey("ctrl",'w')
