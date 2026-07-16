
response = {
    "hello" : "hi",
    "red" : "apple" ,
    "yellow" : "banana",
    "orange" : "malta",
    "abdullah" : "tahir"
    
    
}


while True:
    user_input = input("Enter Text : ")
    clean_input = user_input.lower().strip()
    
    if clean_input == "exit":
        break
    else:
        reply = response.get(clean_input , "Invalid Entery")
        print(reply)
   
    
        
    

    
            
        
        