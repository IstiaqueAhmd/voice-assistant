import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import time

def record_audio(duration=5, sample_rate=16000):
    """Record audio from microphone"""
    print("Recording...")
    try:
        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype='float32'
        )
        sd.wait()
        print("Recording complete")
        return audio.flatten()
    except Exception as e:
        print(f"Recording failed: {e}")
        return None

def save_wav(audio, filename, sample_rate=16000):
    """Save numpy array as WAV file"""
    if audio is None:
        return None
        
    try:
        # Convert float32 to int16
        audio_int16 = np.int16(audio * 32767)
        write(filename, sample_rate, audio_int16)
        print(f"Saved audio to {filename}")
        return filename
    except Exception as e:
        print(f"Failed to save audio: {e}")
        return None