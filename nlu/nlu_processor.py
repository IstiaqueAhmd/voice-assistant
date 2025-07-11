import json
import re

def load_intents(file_path="nlu/intents.json"):
    try:
        with open(file_path) as f:
            return json.load(f)
    except:
        # Fallback intents if file missing
        return {
            "greeting": {
                "patterns": ["hello", "hi", "hey"],
                "responses": ["Hello!", "Hi there!"]
            },
            "fallback": {
                "responses": ["Sorry, I didn't understand that"]
            }
        }

def classify_intent(text, intents):
    text = text.lower().strip()
    
    # Check for exact matches
    for intent, data in intents.items():
        if "patterns" in data:
            for pattern in data["patterns"]:
                if re.fullmatch(pattern.lower(), text):
                    return intent
    
    # Simple keyword matching
    if "time" in text:
        return "time"
    if "joke" in text:
        return "joke"
    
    return "fallback"