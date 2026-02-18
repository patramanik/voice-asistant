# voice-asistant

This is a simple voice assistant script that uses your microphone to listen and perform actions like playing YouTube videos, searching Google, sending WhatsApp messages, and basic system commands.

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

- **Or activate** (Command Prompt / cmd):

```cmd
.venv\Scripts\activate
```

- **Add dependencies**:
```powershell
    pip freeze > requirements.txt
```

- **Install dependencies**:

```powershell
pip install -r requirements.txt
```

- **Run the assistant**:

```powershell
python main.py
```

**Windows-specific note for PyAudio**
- If `pyaudio` fails to build on Windows, install it via `pipwin`:

```powershell
pip install pipwin
pipwin install pyaudio
```

**Troubleshooting**
- If microphone not detected, check Windows privacy settings and that no other app is exclusively using the device.
- For text-to-speech voice selection issues, try changing the index in `voices[1]` in `asistant.py`.
- If WhatsApp automation fails, ensure browser is installed and you are logged into WhatsApp Web.

**Files**
- `asistant.py` — main script
- `requirements.txt` — dependency list

**Git**
- Initialize a new git repository and make the first commit:

```bash
git init
git add .
git commit -m "Initial commit - voice-asistant"
```

- (Optional) Add a remote and push to GitHub/remote:

```bash
git remote add origin <your-repo-URL>
git branch -M main
git push -u origin main
```

- Ensure `.gitignore` exists (it should exclude `.venv/`, `__pycache__/`, `.vscode/`, etc.).

If you want, I can also install the packages into the created `.venv` now.
