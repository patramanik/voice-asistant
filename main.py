import speech_recognition as sr
import pyttsx3

from nlp_model import NLPModel
from entity_extractor import extract_entity
from router import ACTIONS

engine = pyttsx3.init()
engine.setProperty("voice", engine.getProperty("voices")[1].id)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except:
        return ""

nlp = NLPModel("intents.json")

speak("AI Assistant Online")

while True:
    command = take_command()
    if not command:
        continue

    intent = nlp.predict_intent(command)
    entity = extract_entity(command, intent)

    if intent == "EXIT":
        speak("Goodbye")
        break

    speak(f"{intent.replace('_',' ')} {entity}")
    ACTIONS[intent](entity)
