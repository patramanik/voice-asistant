import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import webbrowser
import time

# Initialize the 'voice'
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

def speak(text):
    print(f"Assistant: {text}") # So you can see it in the terminal too
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n--- Listening ---")
        recognizer.pause_threshold = 0.8 # Slightly faster response
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception:
        return "none"

def run_assistant():
    speak("System Online. How can I help you?")
    
    while True:
        command = take_command()

        if 'none' in command:
            continue

        # --- YOUTUBE COMMANDS ---
        if 'play' in command:
            song = command.replace('play', '')
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # --- GOOGLE / SEARCH COMMANDS ---
        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'search' in command or 'google' in command:
            search_query = command.replace('search', '').replace('google', '')
            speak(f"Searching Google for {search_query}")
            pywhatkit.search(search_query)

        # --- WHATSAPP COMMANDS ---
        elif 'whatsapp' in command:
            speak("Who is the message for? Please tell me the phone number with country code.")
            number = take_command().replace(" ", "") # Cleans up spaces in voice-to-number
            
            speak("What is the message?")
            message = take_command()
            
            speak("Sending message now. Please do not touch your mouse.")
            # opens browser and sends after 15 seconds
            pywhatkit.sendwhatmsg_instantly(f"+{number}", message, wait_time=15, tab_close=True)
            speak("Message task completed.")

        # --- SYSTEM COMMANDS ---
        elif 'shutdown' in command or 'turn off computer' in command:
            speak("Confirmed. Shutting down in 10 seconds. Save your work!")
            os.system("shutdown /s /t 10")
            break

        elif 'exit' in command or 'stop' in command or 'bye' in command:
            speak("Goodbye! Have a nice day.")
            break
        
        else:
            print("Command not recognized. Try saying 'Open YouTube' or 'Play Music'.")

if __name__ == "__main__":
    run_assistant()