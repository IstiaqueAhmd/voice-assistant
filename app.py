import os
import datetime
import random
import time
from asr.whisper_asr import transcribe_audio
from nlu.nlu_processor import load_intents, classify_intent
from tts.coqui_tts import setup_tts, text_to_speech
from utils.audio_utils import record_audio, save_wav

class VoiceAssistant:
    def __init__(self):
        self.tts = setup_tts()
        self.intents = load_intents()
        print("Voice assistant initialized")

    def process_command(self, command_text):
        """Process text command and generate response"""
        intent = classify_intent(command_text, self.intents)
        responses = self.intents.get(intent, {}).get("responses", ["I'm not sure how to respond"])
        response = random.choice(responses)
        
        # Handle dynamic responses
        if "{time}" in response:
            current_time = datetime.datetime.now().strftime("%H:%M")
            response = response.format(time=current_time)
        
        return response

    def run_cli(self):
        """Run assistant in CLI mode"""
        print("\nVoice Assistant CLI - Press Ctrl+C to exit")
        print("Speak after the 'Recording...' prompt")
        
        while True:
            try:
                # Record audio
                audio_data = record_audio(duration=5)
                if audio_data is None:
                    continue
                
                # Save temporary file
                input_file = "input_audio.wav"
                save_wav(audio_data, input_file)
                
                # Transcribe audio
                user_input = transcribe_audio(input_file)
                if not user_input:
                    print("No speech detected")
                    continue
                    
                print(f"You said: {user_input}")
                
                # Process command
                response = self.process_command(user_input)
                print(f"Assistant: {response}")
                
                # Convert to speech
                output_file = "response.wav"
                if text_to_speech(self.tts, response, output_file):
                    # Play audio on Windows
                    if os.name == 'nt':
                        os.system(f"start {output_file}")
                    else:
                        print(f"Audio response saved to {output_file}")
                
                # Cleanup
                time.sleep(1)
                
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run_cli()