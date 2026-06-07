# Hello AI - Basic AI Chatbot

print("🤖 Hello! I am AI Bot.")
name = input("What's your name? : ")

print(f"Nice to meet you, {name}!")

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("AI Bot: Hello! How can I help you today?")

    elif "how are you" in user_input:
        print("AI Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user_input:
        print("AI Bot: My name is AI Bot.")

    elif "help" in user_input:
        print("AI Bot: I can chat with you and answer simple questions.")

    elif "good" in user_input:
        print("AI Bot: That's wonderful to hear!")

    elif "bad" in user_input or "sad" in user_input:
        print("AI Bot: I'm sorry to hear that. I hope things improve soon.")

    elif user_input == "bye" or user_input == "exit":
        print(f"AI Bot: Goodbye, {name}! Have a great day!")
        break

    else:
        print("AI Bot: That's interesting! Tell me more.")