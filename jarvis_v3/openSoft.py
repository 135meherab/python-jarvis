import pyautogui

from speak import speak


def openSoftware(command):
    if "start" in command:
        command = command.replace("start","")
        command = command. replace("jarvis","")
        speak("starting "+ command)
        pyautogui.press("super")
        pyautogui.typewrite(command)
        pyautogui.sleep(2)
        pyautogui.press("enter")

