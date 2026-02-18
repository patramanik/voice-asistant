import os
import pywhatkit
import webbrowser
import pyautogui

def open_app(app_name):
    app_name = app_name.lower()
    
    # Try to open as a local application or file
    try:
        os.startfile(app_name)
        print(f"Opening '{app_name}' locally...")
        return
    except FileNotFoundError:
        # Expected if it's not a known command/file
        print(f"'{app_name}' not found locally. Searching web...")
    except Exception as e:
        print(f"Checking web for '{app_name}' (local error: {e})...")

    # Fallback: Open in browser using "I'm Feeling Lucky"
    url = f"https://www.google.com/search?q={app_name}&btnI"
    webbrowser.open(url)
    print(f"Searching for '{app_name}' online...")


def play_music(query):
    pywhatkit.playonyt(query)

def stop_music(query=None):
    pyautogui.press("playpause")
    print("Simulated Play/Pause key press.")

def search_web(query):
    pywhatkit.search(query)

