

def chatbot_response(user_input):
    user_input = user_input.lower()  # Normalize input for easier matching

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    # Asking about well-being
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking."

    # Asking for name
    elif "your name" in user_input:
        return "I'm your friendly chatbot 🤖. You can call me ChatBot!"

    # Farewell
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a wonderful day!"

    # Default response
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"

# Run chatbot in loop
print("ChatBot: Hi! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatBot: Goodbye! 👋")
        break
    response = chatbot_response(user_input)
    print("ChatBot:", response)
