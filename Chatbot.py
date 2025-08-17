print("=====================================")
print("🤖  Welcome to the Python Chatbot  🤖")
print("=====================================")
print("I can chat with you, tell jokes, share my name, and more!")
print("Type 'bye' anytime to exit.\n")

while True:
    user_input = input("You: ").lower()

    if "bye" in user_input:
        print("Chatbot: Goodbye! It was nice talking to you 😊")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello there! How are you doing today?")
    elif "your name" in user_input:
        print("Chatbot: My name is PyBot, your friendly chatbot built with Python!")
    elif "how are you" in user_input:
        print("Chatbot: I'm just code, but I’m feeling awesome today! How about you?")
    elif "fine" in user_input or "good" in user_input or "great" in user_input:
        print("Chatbot: That’s great to hear! Stay positive and keep smiling 😃")
    elif "sad" in user_input or "bad" in user_input or "tired" in user_input:
        print("Chatbot: Oh no! Don’t worry, tough times don’t last but tough people do 💪")
    elif "joke" in user_input:
        print("Chatbot: Sure! Here’s one:")
        print("       Why don’t skeletons fight each other?")
        print("       Because they don’t have the guts! 😂")
    elif "weather" in user_input:
        print("Chatbot: I can’t check the weather yet 🌦️, but I hope it’s nice where you are!")
    elif "help" in user_input or "options" in user_input or "menu" in user_input:
        print("Chatbot: Here are some things you can try:")
        print("         👉 Say 'hello' or 'hi'")
        print("         👉 Ask 'what is your name'")
        print("         👉 Say 'how are you'")
        print("         👉 Ask for a 'joke'")
        print("         👉 Talk about 'weather'")
        print("         👉 Say 'bye' to exit")
    else:
        print("Chatbot: Hmm 🤔 I didn’t understand that. Try asking for 'help' to see options.")
