import pyautogui
import webbrowser

from speak import speak


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
