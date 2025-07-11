from TTS.api import TTS
import torch

def setup_tts():
    try:
        # Use small model for faster startup
        return TTS(model_name="tts_models/en/ljspeech/glow-tts", 
                  progress_bar=False,
                  gpu=torch.cuda.is_available())
    except Exception as e:
        print(f"TTS setup failed: {e}")
        return None

def text_to_speech(tts, text, output_path="output.wav"):
    if tts is None:
        return None
        
    try:
        tts.tts_to_file(text=text, file_path=output_path)
        return output_path
    except Exception as e:
        print(f"TTS failed: {e}")
        return None