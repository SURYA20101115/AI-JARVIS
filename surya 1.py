import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import wikipedia
import os

recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()

def speak(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today sir?")
    elif "what is your name" in command:
        speak("I am your jarvis sir .")
    elif "goodbye" in command:
        speak("Goodbye! sir")
    elif'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif 'date' in command:
        speak('sorry, I have a headache sir')
    elif 'are you single' in command:
        speak('I am in relationship with wifi sir')
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'why' in command:
        speak('i am here to assist you sir')
    elif 'open iron man' in command:
        speak('opening sir')
        os.startfile(r'E:\IRON MAN')
    elif 'daddy' in command:
        speak('opening for you sir')
        os.startfile(C:\Users\WELCOME\Desktop\daddy)
    elif'thank you' in command:
        speak(anytime for you sir)
    else:
        speak("I'm not sure how to respond to that.")

while True:
    command = listen().lower()
    process_command(command)
