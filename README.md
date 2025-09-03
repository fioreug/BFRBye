...
# BFRBye

A simple desktop application for BFRB monitoring. It uses [MediaPipe](https://developers.google.com/mediapipe) to track hands positions and trigger input dialogs.  
Users can write their trigger thoughts or feelings, and save them to a local file (TXT/CSV) or sent to Notion (based on configuration).

---

## Features
- Minimal GUI with **Start** and **Configuration** buttons.
- Detects your hand in the background.
- Opens an input dialog when your hand is in front of your face.
- Makes a beep noise and launches a pop-up for you to log the feelings or thoughts that may have triggered your behavior
- Saves responses to:
  - Local file (`output.csv` or `output.txt`), or
  - Notion database (via API token).
- Configurable through a simple YAML file or GUI.

---

## Windows executable
⚠️ The standalone executable is **not available yet**.  
It will be included in future releases (starting from `v0.2.0`).

For now, please run the application from source (see [Installation](#-installation-for-developers)).


---

## Installation For Developers

Clone the repository and install dependencies:

```bash
git clone https://github.com/fioreug/bfrbye.git
cd bfrbye
pip install -r requirements.txt
```
Run the application:

```bash
python -m bfrbye
```
