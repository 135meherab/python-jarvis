import speech_recognition as sr

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
