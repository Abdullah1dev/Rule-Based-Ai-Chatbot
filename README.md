# 🤖 RuleBot - Rule-Based AI Chatbot

A simple rule-based chatbot built using Python. The chatbot responds to predefined user inputs using a dictionary (hash map) and demonstrates the fundamentals of conversational AI through rule-based decision making.

## 📌 Project Overview

This project was developed as an AI internship task to demonstrate the basic concepts of a rule-based chatbot. It accepts user input, matches it against predefined responses, and continues the conversation until the user chooses to exit.

## ✨ Features

- Handles greetings such as **hello**, **hi**, and **good morning**
- Responds to predefined questions about AI and Python
- Supports the **help** command to display available commands
- Handles unknown inputs with a default response
- Allows users to exit the chatbot using the **exit** command
- Runs continuously until the user exits

## 🛠 Technologies Used

- Python 3
- Dictionaries (Hash Maps)
- Control Flow (`if-else`)
- While Loop
- String Manipulation (`lower()` and `strip()`)

## 📂 Project Structure

```text
RuleBot/
│── chatbot.py
│── README.md
```

## 🚀 How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/RuleBot.git
```

2. Navigate to the project directory.

```bash
cd RuleBot
```

3. Run the chatbot.

```bash
python chatbot.py
```

## 💬 Sample Output

```text
==================================================
        🤖 RuleBot
==================================================
Hello! I'm your Rule-Based AI Chatbot.
I can respond to a set of predefined commands.

Type 'help' to see the available commands.
Type 'exit' to end the conversation.
==================================================

You: hello
Bot: Hello! 👋 How can I help you today?

You: what is ai
Bot: AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.

You: help
Bot:
Available Commands:
- hello
- hi
- hey
- how are you
- what is your name
- what is ai
- what is machine learning
- what is python
- exit

You: exit
Bot: Thank you for chatting with me. Goodbye! 👋
```

## 📚 Concepts Demonstrated

- Rule-Based Chatbot
- Dictionary (Hash Map) Lookup
- Control Flow
- Continuous User Interaction
- Input Normalization
- Basic Conversational Logic

## 👨‍💻 Author

**Abdullah Tahir**

Computer Science Student | AI Engineering Enthusiast
