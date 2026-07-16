


while True:
    user_input = input("Enter Text : ")
    clean_input = user_input.lower().strip()

    
    if clean_input == "hello":
        print("Hi")
    elif clean_input == "tell me about your self":
        print("I am Abdullah Assistant")
    elif clean_input == "what is time":
        print("I dont know")
        
    elif clean_input == "exit":
        break
    
    else:
        print("Invalid Entry.")
        
        