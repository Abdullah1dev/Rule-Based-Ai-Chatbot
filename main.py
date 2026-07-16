
response = {
    "hello" : "hi",
    "red" : "apple" ,
    "yellow" : "banana",
    "orange" : "malta",
    "abdullah" : "tahir"
    
    
}



while True:
    print("=" * 50)
    print("🤖 Rule-Based AI Chatbot")
    print("=" * 50)
    print("Hello! I'm your Rule-Based AI Chatbot.")
    print("I can respond to a set of predefined commands.")
    print("\nType 'help' to see the available commands.")
    print("Type 'exit")
    
    
    
    user_input = input("Enter Text : ")
    clean_input = user_input.lower().strip()
    
    if clean_input == "exit": 
        break
    else:
        reply = response.get(clean_input , "Invalid Entery")
        print(reply)
