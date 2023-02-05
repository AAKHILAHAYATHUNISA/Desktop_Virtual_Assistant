print("hello")
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyaudio
import webbrowser
import os
import smtplib

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
print(voices)
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aakhilahayathunisam.20cse@kongu.edu', 'Bismi@2002')
    server.sendmail('aakhila2002@gmail.com', to, content)
    server.close()
    

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else :
        speak("Good Evening")
    speak("I am Jarvis how may I help YOU")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

        # print("User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        # webbrowser.open(query,".com")
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("Axxording to wikipedia")
            print(results)
            speak(results)
        elif 'com' in query:
            webbrowser.open(query,".com")
            # webbrowser.open('youtube.com') 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "aakhila2002@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend, i couldn't send the email")
        elif 'quit' in query:
            exit()
print("end")

