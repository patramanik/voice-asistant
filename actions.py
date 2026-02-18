import subprocess
import pywhatkit

def open_app(app_name):
    subprocess.Popen(f'start {app_name}', shell=True)

def play_music(query):
    pywhatkit.playonyt(query)

def search_web(query):
    pywhatkit.search(query)
