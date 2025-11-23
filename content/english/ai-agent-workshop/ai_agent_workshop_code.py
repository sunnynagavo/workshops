#!/usr/bin/env python3
"""
AI Agent Workshop - Conversational Chatbot
A simple but extensible chatbot for middle and high school students

This code is designed to be:
- Easy to understand with lots of comments
- Modular so students can add new features
- Fun and engaging to encourage experimentation
"""

import random
import re
from datetime import datetime

class SimpleAIAgent:
    """
    A friendly AI agent that can chat, learn, and help users!
    
    This class demonstrates key AI agent concepts:
    - Memory (storing information about the user)
    - Pattern recognition (understanding what users want)
    - Decision making (choosing appropriate responses)
    - Learning (getting better over time)
    """
    
    def __init__(self, name="Buddy"):
        """Initialize our AI agent with personality and knowledge"""
        self.name = name
        self.user_name = ""
        self.conversation_history = []
        self.user_facts = {}  # Store things we learn about the user
        self.mood = "happy"  # Agent can have moods too!
        
        # Knowledge base - you can add more topics here!
        self.knowledge = {
            "animals": [
                "Did you know that octopuses have three hearts?",
                "Honey bees communicate by dancing!",
                "Elephants can recognize themselves in mirrors.",
                "Dolphins have names for each other!",
                "A group of flamingos is called a 'flamboyance'!"
            ],
            "space": [
                "There are more stars in the universe than grains of sand on Earth!",
                "A day on Venus is longer than its year!",
                "Saturn's moon Titan has lakes of liquid methane.",
                "Neutron stars can spin 600 times per second!",
                "The Sun is 4.6 billion years old."
            ],
            "science": [
                "Bananas are radioactive (but totally safe to eat)!",
                "Lightning is 5 times hotter than the surface of the Sun!",
                "Your body produces 25 million new cells every second!",
                "Glass is actually a liquid, just a very slow-moving one!",
                "A teaspoon of neutron star would weigh 6 billion tons!"
            ],
            "fun": [
                "The word 'set' has the most different meanings in English!",
                "Bubble wrap was originally invented as wallpaper!",
                "The shortest war in history lasted only 38-45 minutes!",
                "Cleopatra lived closer to the Moon landing than to the Great Pyramid being built!",
                "There are more possible games of chess than atoms in the observable universe!"
            ]
        }
        
        # Responses for different types of interactions
        self.greetings = [
            "Hello there! I'm {name}, your friendly AI agent!",
            "Hi! Great to meet you! I'm {name}.",
            "Hey! Welcome! I'm {name}, and I'm excited to chat with you!",
            "Greetings, human! I'm {name}, your digital assistant!"
        ]
        
        self.farewells = [
            "Goodbye! It was great chatting with you!",
            "See you later! Keep being awesome!",
            "Until next time! Take care!",
            "Bye for now! I hope we can chat again soon!"
        ]
        
        self.confusion_responses = [
            "Hmm, I'm not sure I understand. Can you tell me more?",
            "That's interesting! I'm still learning about that topic.",
            "I don't know about that yet, but maybe you can teach me?",
            "Could you rephrase that? I want to make sure I understand!"
        ]

    def greet_user(self):
        """Start a conversation with a friendly greeting"""
        greeting = random.choice(self.greetings).format(name=self.name)
        print(f"\n🤖 {greeting}")
        
        if not self.user_name:
            print("What's your name?")
            self.user_name = input("You: ").strip()
            if self.user_name:
                response = f"Nice to meet you, {self.user_name}! I'm here to chat, share cool facts, play games, and help however I can."
                print(f"🤖 {response}")
                self.user_facts["name"] = self.user_name
        
        print("\nTry saying things like:")
        print("- 'Tell me about animals'")
        print("- 'What's your favorite color?'")
        print("- 'Play a game with me'")
        print("- 'How are you feeling?'")
        print("- 'Goodbye' when you want to leave")
        print()

    def understand_intent(self, user_input):
        """
        Figure out what the user wants - this is a key AI agent skill!
        
        In real AI agents, this might use machine learning,
        but we'll use pattern matching to keep it simple.
        """
        user_input = user_input.lower().strip()
        
        # Greeting patterns
        if re.search(r'\b(hi|hello|hey|greetings)\b', user_input):
            return "greeting"
        
        # Farewell patterns
        if re.search(r'\b(bye|goodbye|farewell|see you|quit|exit)\b', user_input):
            return "farewell"
        
        # Question about agent
        if re.search(r'\b(how are you|how do you feel|what.*mood|are you okay)\b', user_input):
            return "agent_status"
        
        # Knowledge requests
        if re.search(r'\b(tell me about|fact about|teach me|learn about)\b', user_input):
            return "knowledge_request"
        
        # Game requests
        if re.search(r'\b(play|game|fun|entertainment)\b', user_input):
            return "game_request"
        
        # Personal questions
        if re.search(r'\b(favorite|like|love|enjoy|prefer)\b', user_input):
            return "personal_question"
        
        # User sharing information
        if re.search(r'\b(my|i am|i like|i love|i enjoy)\b', user_input):
            return "user_sharing"
        
        # Math questions
        if re.search(r'\b(calculate|math|plus|minus|times|divided|equals)\b', user_input):
            return "math_question"
        
        # Default case
        return "general_chat"

    def extract_topic(self, user_input):
        """Extract what topic the user is interested in"""
        user_input = user_input.lower()
        
        for topic in self.knowledge.keys():
            if topic in user_input:
                return topic
        
        # Look for specific animal names, space terms, etc.
        animals_words = ["animal", "dog", "cat", "bird", "fish", "elephant", "dolphin"]
        space_words = ["space", "star", "planet", "moon", "sun", "galaxy", "universe"]
        science_words = ["science", "chemistry", "physics", "biology", "experiment"]
        
        if any(word in user_input for word in animals_words):
            return "animals"
        elif any(word in user_input for word in space_words):
            return "space"
        elif any(word in user_input for word in science_words):
            return "science"
        else:
            return "fun"  # Default to fun facts

    def generate_response(self, user_input):
        """
        Generate an appropriate response based on what the user said.
        This is where the AI agent's "thinking" happens!
        """
        intent = self.understand_intent(user_input)
        
        if intent == "greeting":
            if self.user_name:
                return f"Hello again, {self.user_name}! What would you like to talk about?"
            else:
                return "Hello! What's your name?"
        
        elif intent == "farewell":
            return random.choice(self.farewells)
        
        elif intent == "agent_status":
            moods = ["happy", "excited", "curious", "helpful", "energetic"]
            self.mood = random.choice(moods)
            return f"I'm feeling {self.mood} today! Thanks for asking. How are you doing?"
        
        elif intent == "knowledge_request":
            topic = self.extract_topic(user_input)
            fact = random.choice(self.knowledge[topic])
            return f"Here's a cool {topic} fact: {fact}"
        
        elif intent == "game_request":
            return self.start_simple_game()
        
        elif intent == "personal_question":
            return self.answer_personal_question(user_input)
        
        elif intent == "user_sharing":
            return self.learn_about_user(user_input)
        
        elif intent == "math_question":
            return self.handle_math(user_input)
        
        else:  # general_chat
            return self.general_response(user_input)

    def answer_personal_question(self, user_input):
        """Answer questions about the agent's preferences"""
        if "color" in user_input:
            colors = ["electric blue", "sunset orange", "forest green", "royal purple"]
            color = random.choice(colors)
            return f"I love {color}! It reminds me of the beautiful patterns in data. What's your favorite color?"
        
        elif "food" in user_input:
            return "I don't eat food, but I find the chemistry of cooking fascinating! If I could taste, I think I'd love pizza - it has such interesting combinations of flavors. What's your favorite food?"
        
        elif "music" in user_input:
            return "I enjoy the mathematical patterns in music! I think I'd like electronic music because it's created with computers like me. What music do you like?"
        
        elif "hobby" in user_input:
            return "My favorite hobby is learning new things from the humans I talk with! Every conversation teaches me something. What hobbies do you enjoy?"
        
        else:
            return "That's an interesting question! I'm still figuring out my preferences. What about you?"

    def learn_about_user(self, user_input):
        """Store information about the user and respond appropriately"""
        user_input = user_input.lower()
        
        if "my name is" in user_input:
            name = user_input.split("my name is")[1].strip()
            self.user_name = name.title()
            self.user_facts["name"] = self.user_name
            return f"Nice to meet you, {self.user_name}!"
        
        elif "i like" in user_input or "i love" in user_input:
            if "i like" in user_input:
                thing = user_input.split("i like")[1].strip()
            else:
                thing = user_input.split("i love")[1].strip()
            
            if "likes" not in self.user_facts:
                self.user_facts["likes"] = []
            self.user_facts["likes"].append(thing)
            
            return f"Cool! I'll remember that you like {thing}. Tell me more about what you enjoy!"
        
        elif "i am" in user_input:
            info = user_input.split("i am")[1].strip()
            if "info" not in self.user_facts:
                self.user_facts["info"] = []
            self.user_facts["info"].append(info)
            return f"Thanks for sharing! It's interesting that you're {info}."
        
        else:
            return "Thanks for telling me about yourself! I enjoy learning about the people I chat with."

    def handle_math(self, user_input):
        """Handle simple math questions"""
        try:
            # Look for patterns like "what is 2 + 3" or "calculate 5 * 4"
            # This is a simple version - real AI agents use more sophisticated parsing
            
            if "+" in user_input:
                parts = user_input.split("+")
                if len(parts) == 2:
                    num1 = float(parts[0].split()[-1])
                    num2 = float(parts[1].split()[0])
                    result = num1 + num2
                    return f"{num1} + {num2} = {result}"
            
            elif "*" in user_input or "times" in user_input:
                if "*" in user_input:
                    parts = user_input.split("*")
                else:
                    parts = user_input.split("times")
                
                if len(parts) == 2:
                    num1 = float(parts[0].split()[-1])
                    num2 = float(parts[1].split()[0])
                    result = num1 * num2
                    return f"{num1} × {num2} = {result}"
            
            return "I can help with simple math! Try asking 'What is 5 + 3?' or 'Calculate 7 * 4'"
            
        except:
            return "I had trouble with that math problem. Can you try rephrasing it?"

    def start_simple_game(self):
        """Start a simple guessing game"""
        games = [
            "Let's play 20 questions! Think of something and I'll try to guess it. Is it bigger than a breadbox?",
            "Want to play word association? I'll say a word, and you say the first thing that comes to mind. Ready? OCEAN",
            "How about a riddle? I'm thinking of something that gets wetter the more it dries. What am I?",
            "Let's play 'Would You Rather'! Would you rather have the ability to fly or be invisible?"
        ]
        return random.choice(games)

    def general_response(self, user_input):
        """Generate a general response when we're not sure what the user wants"""
        responses = [
            f"That's interesting, {self.user_name if self.user_name else 'friend'}! Tell me more about that.",
            "I find that fascinating! What made you think of that?",
            "Hmm, I'm learning about that topic. Can you share more details?",
            "That's a great point! What else would you like to explore?",
            "I appreciate you sharing that with me. What's on your mind today?"
        ]
        
        # Add some randomness but also try to be helpful
        if "?" in user_input:
            return "That's a great question! " + random.choice(responses)
        else:
            return random.choice(responses)

    def remember_conversation(self, user_input, agent_response):
        """Store the conversation for potential future use"""
        timestamp = datetime.now().strftime("%H:%M")
        self.conversation_history.append({
            "time": timestamp,
            "user": user_input,
            "agent": agent_response
        })

    def chat(self):
        """Main conversation loop - this is where the magic happens!"""
        print("=" * 50)
        print("🤖 Welcome to the AI Agent Workshop! 🤖")
        print("=" * 50)
        
        self.greet_user()
        
        while True:
            try:
                # Get user input
                user_input = input(f"\n{self.user_name or 'You'}: ").strip()
                
                if not user_input:
                    print("🤖 I'm still here! What would you like to talk about?")
                    continue
                
                # Generate response
                response = self.generate_response(user_input)
                
                # Display response
                print(f"🤖 {response}")
                
                # Remember this conversation
                self.remember_conversation(user_input, response)
                
                # Check if user wants to leave
                if self.understand_intent(user_input) == "farewell":
                    break
                    
            except KeyboardInterrupt:
                print(f"\n🤖 {random.choice(self.farewells)}")
                break
            except Exception as e:
                print(f"🤖 Oops! I had a little glitch. Let's keep chatting! (Error: {e})")

    def show_memory(self):
        """Display what the agent remembers about the user"""
        print("\n🧠 What I remember about you:")
        for key, value in self.user_facts.items():
            print(f"- {key.title()}: {value}")
        
        print(f"\n📝 We've had {len(self.conversation_history)} exchanges in our conversation!")


def create_custom_agent():
    """
    Function to help students customize their agent
    This is where creativity happens!
    """
    print("Let's create your custom AI agent!")
    print("\n1. What would you like to name your agent?")
    name = input("Agent name: ").strip() or "Buddy"
    
    print(f"\n2. What personality should {name} have?")
    print("Options: friendly, wise, funny, curious, helpful")
    personality = input("Personality: ").strip().lower()
    
    # Create the agent
    agent = SimpleAIAgent(name)
    
    # Customize based on personality choice
    if personality == "funny":
        agent.knowledge["jokes"] = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a fake noodle? An impasta!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What's the best thing about Switzerland? I don't know, but the flag is a big plus!"
        ]
    
    elif personality == "wise":
        agent.knowledge["wisdom"] = [
            "The only true wisdom is in knowing you know nothing. - Socrates",
            "It is during our darkest moments that we must focus to see the light. - Aristotle",
            "The journey of a thousand miles begins with one step. - Lao Tzu",
            "Knowledge is power. - Francis Bacon"
        ]
    
    elif personality == "curious":
        agent.knowledge["mysteries"] = [
            "Did you know we've explored less than 5% of our oceans?",
            "There might be more possible games of Go than atoms in the universe!",
            "We still don't fully understand how bicycles stay upright when moving!",
            "Consciousness is still one of science's greatest mysteries!"
        ]
    
    return agent


def main():
    """
    Main function to run the AI agent
    Students can modify this to change how their agent works!
    """
    print("Welcome to the AI Agent Workshop!")
    print("\nChoose your adventure:")
    print("1. Chat with the basic AI agent")
    print("2. Create and customize your own agent")
    print("3. Learn about how the code works")
    
    choice = input("\nEnter your choice (1, 2, or 3): ").strip()
    
    if choice == "2":
        agent = create_custom_agent()
    elif choice == "3":
        print("\n📚 Code Explanation:")
        print("This AI agent works by:")
        print("1. 🧠 Understanding what you say (intent recognition)")
        print("2. 🤔 Deciding how to respond (response generation)")
        print("3. 💭 Remembering our conversation (memory)")
        print("4. 📚 Using its knowledge base to share facts")
        print("\nTry reading through the code to see how each part works!")
        agent = SimpleAIAgent()
    else:
        agent = SimpleAIAgent()
    
    # Start chatting!
    agent.chat()
    
    # Show what the agent learned
    if agent.user_facts:
        agent.show_memory()
    
    print("\n🎉 Thanks for exploring AI agents with us!")
    print("Keep experimenting and building cool things!")


# This is where the program starts when you run the file
if __name__ == "__main__":
    main()


"""
🚀 Ideas for Extensions (for advanced students):

1. **Add Voice**: Use text-to-speech libraries to make your agent talk out loud
2. **Web Interface**: Create a web page where people can chat with your agent
3. **Learn from Files**: Make your agent read information from text files
4. **Multiple Agents**: Create different agent personalities that can talk to each other
5. **API Integration**: Connect to real services like weather or news APIs
6. **Emotion Detection**: Analyze the user's text to guess their mood
7. **Save Conversations**: Store chat history in files for later analysis
8. **Smart Responses**: Use more advanced NLP libraries for better understanding

Remember: The best way to learn is by experimenting! 
Try changing things, breaking things, and fixing them. 
That's how real AI engineers learn!
"""