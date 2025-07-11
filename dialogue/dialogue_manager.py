import random
import datetime
import json

class DialogueManager:
    def __init__(self, intents_file="nlu/intents.json"):
        self.intents = self._load_intents(intents_file)
    
    def _load_intents(self, file_path):
        with open(file_path) as f:
            return json.load(f)
    
    def generate_response(self, intent):
        responses = self.intents[intent]["responses"]
        response = random.choice(responses)
        
        # Handle dynamic responses
        if "{time}" in response:
            current_time = datetime.datetime.now().strftime("%H:%M")
            response = response.format(time=current_time)
        
        return response