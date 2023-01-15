
from speak import speak


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
