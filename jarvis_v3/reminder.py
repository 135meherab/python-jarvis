import pyttsx3

jarvis=pyttsx3.init("sapi5")
voices=jarvis.getProperty("voices")
jarvis.setProperty('voice',voices[0].id)
jarvis.setProperty('rate',170)


def speak(audio):
    jarvis.say(audio)
    jarvis.runAndWait()


def reminder_msg(command):
    if 'remember' in command:
        remember_msg = command.replace("jarvis",'')
        remember_msg = remember_msg.replace('remember','')
        remember_msg = remember_msg.replace('that','')
        remember_msg = remember_msg.replace('i','you')
        print(remember_msg)
        speak("you told me to remember" + remember_msg)
        remember=open("remember.txt","w")
        remember.write(remember_msg)
        remember.close()
