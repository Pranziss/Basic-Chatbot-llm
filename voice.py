import edge_tts
import asyncio
import os
import platform
import subprocess
from datetime import datetime

# 🎤 Nova's voice by mood
voice_map = {
    "gentle": "en-US-JennyNeural",
    "snarky": "en-US-DavisNeural",
    "goofy": "en-GB-LibbyNeural",
    "chill": "en-US-AriaNeural",
    "curious": "fil-PH-BlessicaNeural"
}

# 🧠 TTS synthesis with fail protection
async def synthesize(text, mood="gentle", filename="nova_voice.mp3"):
    if not text.strip():
        print("[⚠️] TTS received empty text.")
        return None

    voice = voice_map.get(mood, "en-US-JennyNeural")

    if os.path.exists(filename):
        try:
            os.remove(filename)
        except PermissionError:
            print(f"[⚠️] Couldn't delete {filename}. Likely still open.")
            return None

    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(filename)
        return filename
    except Exception as e:
        print(f"[❌] TTS failed: {e}")
        return None

# 🔊 Playback without file locking
def play_voice(filename="nova_voice.mp3"):
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["start", "", filename], shell=True)
        elif platform.system() == "Darwin":
            subprocess.Popen(["afplay", filename])
        else:
            subprocess.Popen(["mpg123", filename])
    except Exception as e:
        print(f"[⚠️] Voice playback error: {e}")