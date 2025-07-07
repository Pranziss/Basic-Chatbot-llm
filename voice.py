from TTS.api import TTS
import os

# Load XTTS model once
print("[XTTS] Loading model...")
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
print("[XTTS] Model loaded.")

# Path to your cloned voice sample
SPEAKER_WAV = os.path.join(os.path.dirname(__file__), "voice_sample.wav")

def synthesize(text, language="en", output_path="output.wav"):
    try:
        print(f"[XTTS] Synthesizing: {text}")
        print(f"[XTTS] Using voice sample: {SPEAKER_WAV}")
        tts.tts_to_file(
            text=text,
            speaker_wav=SPEAKER_WAV,
            language=language,
            file_path=output_path
        )
        print(f"[XTTS] Audio saved to: {output_path}")
    except Exception as e:
        print(f"[XTTS ERROR] {e}")

def play_voice(path="output.wav"):
    try:
        print(f"[XTTS] Playing: {path}")
        os.system(f'start {path}')  # Windows-only playback
    except Exception as e:
        print(f"[PLAYBACK ERROR] {e}")