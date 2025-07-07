from TTS.api import TTS
import os

# Load the XTTS model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# Path to your voice sample
voice_sample = "voice_sample.wav"  # Make sure this file exists in the same folder

# Output path
output_path = "output.wav"

# Text to synthesize
text = "Hello Franz, this is XTTS speaking."

# Generate speech
tts.tts_to_file(
    text=text,
    speaker_wav=voice_sample,
    language="en",
    file_path=output_path
)

# Play the result (Windows only)
os.system(f'start {output_path}')