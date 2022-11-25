import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit


jarvis = pyttsx3.init('sapi5')
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice',voices[0].id)


def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()

#this function wish me according to the systme time
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("Good morning,sir!")
    elif hour >12 and hour <=18:
        speak("Good afternoon,sir")
    else:
        speak("Goog Evening,sir")
    speak("This is jarvis. Your parsonal assistant. How can I help you? ")

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("lintening.....")
        listener.pause_threshold=2
        listener.energy_threshold=600
        voice = listener.listen(source)

    try:
        print('recognizing.....')
        command = listener.recognize_google(voice,language= 'en-bd')
        print('User Command: '+command)
        if 'jarvis' in command:
            command = command.replace('jarvis','')
            print('Command taken: ' + command)

    except Exception as e:
        return 'None'
    return command


if __name__ == '__main__':
    wishme()
    while True:
        command = take_command().lower()


        if 'what\'s your name' in command:
            print('my name is jarvis.')
            speak('my name is jarvis.')
        elif 'who are you' in command:
            print('I am jarvis. your parsonal assistant.')
            speak('I am jarvis. your parsonal assistant.')
        elif 'who is your creator' in command:
            print('fci 15 batch group')
            speak('fci 15 batch group')
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('current time is: ' + time)
        elif 'play on youtube' in command:
            song = command.replace('play on youtube', '')
            speak("playing " + song)
            pywhatkit.playonyt(song)
        elif 'tell me about' in command:
            looking = command.replace('tell me about', '')
            speak('Searching on Wikipedia...... ')
            information = wikipedia.summary(looking, 2)
            print(information)
            speak(information)
        elif 'search for' in command:
            topic = command.replace('search for', '')
            print("Opening google & Searching.......")
            speak('Opening google & Searching')
            pywhatkit.search(topic)
        elif 'play music' in command:
            muiscdir = 'E:\\WondershareUniConverter\\Downloaded\\Nasheed'
            songs = os.listdir(muiscdir)
            print(songs)
            os.startfile(os.path.join(muiscdir, songs[0]))
        elif 'open' in command:
            site = command.replace('open', '')
            webbrowser.open_new_tab(site)
            speak('opening ' + site)
        elif 'start code' in command:
            code = "C:\\Users\\M3H3RA8$ PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
        elif 'start pycharm' in command:
            pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe"
            os.startfile(pycharm)
        elif 'check telegram' in command:
            telegram = "C:\\Users\\M3H3RA8$ PC\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(telegram)
        else:
            speak("I can't recognize your command. Please say that again.")

