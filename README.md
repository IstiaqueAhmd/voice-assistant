voice-assistant/
├── asr/
│   ├── whisper_asr.py        # Speech-to-text with Whisper
├── nlu/
│   ├── intents.json          # Intent definitions
│   ├── nlu_processor.py      # spaCy-based intent classifier
├── dialogue/
│   ├── dialogue_manager.py   # Conversation flow logic
├── tts/
│   ├── coqui_tts.py          # Text-to-speech synthesis
├── utils/
│   ├── audio_utils.py        # Audio processing helpers
├── app.py                    # Main application entry point
└── requirements.txt          # Python dependencies