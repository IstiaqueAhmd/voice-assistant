import whisper

def transcribe_audio(audio_path, model_size="base.en"):
    try:
        model = whisper.load_model(model_size)
        result = model.transcribe(audio_path)
        return result["text"].strip()
    except Exception as e:
        print(f"Transcription failed: {e}")
        return ""