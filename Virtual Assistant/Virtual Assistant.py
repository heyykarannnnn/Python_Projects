import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import subprocess
import platform
import os

# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to listen to user's voice command
def get_Command():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text = text.lower()
            print("You said: ", text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}")

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Intro Screen

print("=====================================    Virtual Assistant    =====================================")
print("*                                                                                                 *")
print("*                                                                                                 *")
print("========================================= By: Karan Sethi =========================================")


# Main loop
while True:
    command = get_Command()
    if command:
        if command == "hello":
            print("Hello! How can I assist you?")
            speak("Hello! How can I assist you?")

        elif command == "who are you":
            print("I am your virtual assistant.")
            speak("I am your virtual assistant.")

        elif command == "what can you do" or command == "help" or command == "introduce yourself":
            print("A Virtual Assistant Developed By Karan Sethi,I can open Google, open Terminal, open Visual Studio Code, open Spotify, open Whatsapp, open YouTube, search for anything on Google, tell you the current time and say goodbye.")
            speak("A Virtual Assistant Developed By Karan Sethi,I can open Google, open Terminal, open Visual Studio Code, open Spotify, open Whatsapp, open YouTube, search for anything on Google, tell you the current time and say goodbye.")
            

        elif command == "goodbye":
            print("Goodbye!")
            speak("Goodbye!")
            break

        elif command == "open google":
            webbrowser.open("https://www.google.com")
            print("Opening Google.")
            speak("Opening Google.")

        elif "open terminal" in command:
            print("Opening Terminal.")
            speak("Opening Terminal.")
            if platform.system() == "Windows":
                os.system("start cmd /k")
            elif platform.system() == "Linux":
                subprocess.Popen(["gnome-terminal"])

        elif "open vs code" in command:
            subprocess.Popen(["code"])
            print("Opening Visual Studio Code.")
            speak("Opening Visual Studio Code.")

        elif "open spotify" in command:
            subprocess.Popen(["spotify"])
            print("Opening Spotify.")
            speak("Opening Spotify.")

        elif "whatsapp" in command:
            webbrowser.open("https://web.whatsapp.com")
            print("Opening Whatsapp.")
            speak("Opening Whatsapp.")

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            print("Opening YouTube.")
            speak("Opening YouTube.")

        elif "search for" in command:
            query = command.replace("search for", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            print(f"Searching for {query}.")
            speak(f"Searching for {query}.")

        elif "what time is it" in command or command == "time":
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            speak(f"The time is {now}.")
            print(f"The time is {now}.")

        else:
            print("Sorry, I don't understand that command.")
            print("Opening Google.")
            webbrowser.open("https://www.google.com")
            speak("Sorry, I don't understand that command.")
            speak("Opening Google.")