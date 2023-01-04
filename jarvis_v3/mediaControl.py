import pyautogui
from pynput import keyboard
from pynput.keyboard import Key,Controller
from time import sleep


def pause(command):
    if "pause" in command:
        pyautogui.press("k")


def play(command):
    if "play" in command:
        pyautogui.press("k")

def mute():
    pyautogui.press("m")

def unmute():
    pyautogui.press("m")

keyboard = Controller()


def volumeup():
        for i in range(5):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            sleep(0.1)


def volumedown():
        for i in range(5):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            sleep(0.1)