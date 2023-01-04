import os

def openSoftware(command):
    if "start telegram" in command:
        telegram = "C:\\Users\\This PC\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
        os.startfile(telegram)
    elif "start pycharm" in command:
        pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe"
        os.startfile(pycharm)
    elif "start music" in command:
        musicdir = "C:\\Users\\This PC\\Downloads\\Music"
        songs = os.listdir(musicdir)
        os.startfile(os.path.join(musicdir, songs[0]))
    elif "start code" in command:
        vsCode = "C:\\Users\\This PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vsCode)