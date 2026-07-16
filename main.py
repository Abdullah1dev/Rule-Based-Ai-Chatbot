
responses = {
    
    
    "hello": "Hello! 👋 How can I help you today?",
    "hi": "Hi there! 😊",
    "hey": "Hey! Nice to meet you.",
    "good morning": "Good morning! Have a wonderful day.",
    "good evening": "Good evening! How can I assist you?",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I'm RuleBot, a Rule-Based AI Chatbot.",
    "who made you": "I was created by Abdullah Tahir using Python.",
    "thank you": "You're welcome! 😊",
    "thanks": "Happy to help!",
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI where computers learn patterns from data.",
    "what is python": "Python is a popular programming language used for AI, web development, automation, and data science.",
    "what is a dictionary": "A dictionary stores data as key-value pairs and provides fast lookup.",
    "help":
    """
    Available Commands:
    - hello
    - hi
    - how are you
    - what is ai
    - what is python
    - who made you
    - tell me a joke
    - exit
    """
    
}

print("=" * 50)
print("🤖 Rule-Based AI Chatbot")
print("=" * 50)
print("Hello! I'm your Rule-Based AI Chatbot.")
print("I can respond to a set of predefined commands.")
print("\nType 'help' to see the available commands.")
print("Type 'exit")



while True:
    
    user_input = input("Enter Text : ")
    clean_input = user_input.lower().strip()
    
    if clean_input == "exit": 
        break
    else:
        reply = responses.get(clean_input , "Invalid Entery")
        print(reply)
