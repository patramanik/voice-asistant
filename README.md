# voice-asistant

This is a versatile voice assistant script that uses your microphone to listen and perform actions like opening any application, playing/pausing music, searching the web, and more.

**Key Features**
- **Smart Open**: Can open *any* application or website. If an app isn't found locally, it automatically searches and opens the official website.
- **Media Control**: Voice commands to stop/pause/play music globally (Youtube, Spotify, etc.).
- **Web Search**: Google search integration.

**Requirements**
- Python 3.8+ installed
- A working microphone and internet connection

**Setup & Run**

- **Create virtual environment** (Windows PowerShell):

```powershell
python -m venv .venv
```

- **Activate** (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

- **Install dependencies**:

```powershell
pip install -r requirements.txt
pip install pyautogui
```

- **Run the assistant**:

```powershell
python main.py
```

**Commands**

| Intent | Purpose | Examples |
| :--- | :--- | :--- |
| **OPEN_APP** | Opens local apps or websites | "Open Notepad", "Open Gmail", "Open Youtube", "Open VS Code" |
| **PLAY_MUSIC** | Plays video on YouTube | "Play music", "Play Ariijt Singh" |
| **STOP_MUSIC** | Pauses/Plays current media | "Stop", "Pause music", "Shut up" |
| **SEARCH_WEB** | Google Search | "Search Python tutorial", "Google weather" |
| **EXIT** | Closes the assistant | "Exit", "Bye" |

**Troubleshooting**
- If microphone not detected, check Windows privacy settings.
- "Stop" command simulates the `Play/Pause` media key on your keyboard. Ensure your media player supports this key.
