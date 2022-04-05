from ctypes import sizeof
from unittest import result
from datetime import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import smtplib
import pyttsx3
import pyjokes
import random
import os


engine = pyttsx3.init('sapi5')


password = 0


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 190)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty(
    'volume')  # getting to know current volume level (min=0 and max=1)
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1


"""Voices"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning sir")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")

    else:
        speak("Good evening, sir")

    speak("My name is Ultron, how can I help?")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening, you can speak now")
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        speak("Recognising your words,please wait")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # engine.save_to_file(query, "test.mp3")
        # engine.runAndWait()
        # speak(query)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("I am sorry, say that again please!")
        return "None"
    return query


global count


def sec(count):

    r = sr.Recognizer()

    with sr.Microphone() as source:
        # speak("I am listening, you can speak now")
        if count == 0:
            speak("Welcome User!, confirm the password")
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        elif count > 0:
            speak("Password not matched!, Try again!")
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

    try:
        speak("Recognising,please wait")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

        print(f"User said: {query}\n")
        query = query.lower()
        if 'google' in query:
            speak("password matched,Welcome to board Sarthak!")
            password = 1

        else:
            count = count+1
            sec(count)

    except Exception as e:
        # print(e)

        print("Say that again please...")
        # speak("I am sorry, say that again please!")
        sec(count)


def takeInterCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        # speak("I am listening, you can speak now")
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        speak("Recognising,please wait")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("I am sorry, say that again please!")
        takeInterCommand()


def sendEmail(to, content):

    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sarthakiet2019@gmail.com', 'your-password')
    server.sendmail('sarthakiet2019@gmail.com', to, content)
    server.close()


if __name__ == "__main__":

    sec(0)

    wishMe()

    cond = True
    while cond:
        query = takeCommand().lower()
        extra = ''

        if 'wikipedia' in query:
            speak("searcing Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube, please wait!")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google,please wait!")
            webbrowser.open("google.com")

        elif 'stack overflow' in query:
            speak("opening stack overflow, please wait!")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("playing your favourite musics!")
            music_dir = 'C:\\Users\\dell.DESKTOP-9INKTNB\\Desktop\\Ultron AI project\\favsongs'
            songs = os.listdir(music_dir)
            # print(songs)
            len = 10
            gen = random.randrange(0, len-1)
            os.startfile(os.path.join(music_dir, songs[gen]))

        elif 'the time' in query:
            strtime = datetime.now().strftime("%H:%M")
            speak(f"Sir,the time is {strtime}")

        elif 'open code' in query:
            speak("opening vscode, please wait!")
            codepath = "F:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        # elif 'send email' in query:
        #     try:
        #         speak("what should i say?")
        #         content = takeCommand()
        #         to = "sarthakiet2019@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("I can't send the email right now, there is some error")

        elif 'tell me a joke' in query:

            My_joke = pyjokes.get_joke(language="en", category="neutral")
            print(My_joke)
            speak(My_joke)

        elif 'shut down' in query:
            speak("closing the system, time to go, bye")
            cond = False

        elif 'shutdown' in query:
            speak("closing the system, time to go, bye")
            cond = False
