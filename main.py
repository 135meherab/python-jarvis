import os
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser
listener = sr.Recognizer()
jarvis = pyttsx3.init()

#reading my command
def talk(text):
    jarvis.say(text)
    jarvis.runAndWait()

#wishing me according to time
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour<=12:
        talk('Good morning sir!')
    elif hour > 12 and hour <=18:
        talk('Good afternoon sir!')
    else:
        talk('Good evening sir!')
    talk('This is jarvis, Your parsonal assistent. How can I help you?')

# taking command using system microphone
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.............')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)


    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is: '+time)
    elif 'play' in command:
        song = command.replace('play','')
        talk("playing "+ song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        looking = command.replace('tell me about', '')
        talk('Searching on Wikipedia...... ')
        information=wikipedia.summary(looking,2)
        print(information)
        talk(information)
    elif 'search for' in command:
        topic = command.replace('search for','')
        print("Opening google & Searching.......")
        talk('Opening google & Searching')
        pywhatkit.search(topic)
    elif 'music' in command:
        muiscdir ='E:\\WondershareUniConverter\\Downloaded\\Nasheed'
        songs = os.listdir(muiscdir)
        print(songs)
        os.startfile(os.path.join(muiscdir,songs[0]))
    elif 'open' in command:
        site=command.replace('open','')
        webbrowser.open_new_tab(site)
        talk('opening '+ site)
    elif 'start code' in command:
        code="C:\\Users\\M3H3RA8$ PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code)
    elif 'pycharm' in command:
        pycharm="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe"
        os.startfile(pycharm)
    else:
        talk("I can't recognize your command. i am searching for it.")
        pywhatkit.search(command)


if __name__ == '__main__':

    wishme()
    while True:
        run_jarvis()