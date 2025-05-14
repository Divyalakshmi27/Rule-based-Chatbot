import re
import random

class SimpleChatbot:
    def _init_(self):
        # Define patterns and responses
        self.patterns = {
            # Greetings
            r'hi|hello|hey|greetings': [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! Nice to meet you!"
            ],
            
            # How are you
            r'how are you|how\'s it going|how do you do': [
                "I'm doing great, thanks for asking!",
                "I'm fine, how about you?",
                "All good! How are you doing?"
            ],
            
            # Name
            r'what is your name|who are you|what should i call you': [
                "I'm ChatBot, nice to meet you!",
                "You can call me ChatBot!",
                "I'm ChatBot, your friendly AI assistant!"
            ],
            
            # Capabilities
            r'what can you do|help|what are your features': [
                "I can chat with you about various topics!",
                "I'm here to have a friendly conversation with you.",
                "I can help you with basic conversation and answer simple questions."
            ],
            
            # Weather
            r'weather|temperature|forecast': [
                "I'm sorry, I don't have access to weather information.",
                "I can't check the weather, but I hope it's nice where you are!",
                "I wish I could tell you about the weather, but I'm not connected to weather services."
            ],
            
            # Time
            r'time|what time is it|current time': [
                "I don't have access to the current time.",
                "I can't tell you the exact time, but I hope you're having a good day!",
                "I'm not connected to a clock, but I'm here to chat whenever you need!"
            ],
            
            # Thanks
            r'thank|thanks|appreciate': [
                "You're welcome!",
                "Happy to help!",
                "Anytime!"
            ],
            
            # Goodbye
            r'bye|goodbye|see you|exit|quit': [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! Come back anytime!"
            ]
        }
        
        # Default responses for when no pattern matches
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more about that.",
            "I'm still learning. Could you explain that differently?",
            "That's a bit beyond my capabilities right now.",
            "I'm not quite sure how to respond to that."
        ]

    def get_response(self, user_input):
        # Convert input to lowercase and remove extra spaces
        user_input = user_input.lower().strip()
        
        # Check each pattern
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        # If no pattern matches, return a random default response
        return random.choice(self.default_responses)

def main():
    chatbot = SimpleChatbot()
    print("ChatBot: Hello! I'm a simple chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye', 'byee', 'goodbye']:
            print("\nChatBot:", chatbot.get_response(user_input))
            break
        
        response = chatbot.get_response(user_input)
        print("\nChatBot:", response)

if _name_ == "_main_":
    main()
