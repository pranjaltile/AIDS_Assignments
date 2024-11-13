import random

# Basic responses for customer queries
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I help you with?", "Hello! Need any assistance?"],
    "store_hours": ["Our store hours are from 9 AM to 9 PM, Monday through Saturday.", "We are open from 9 AM to 9 PM every day except Sunday."],
    "return_policy": ["You can return items within 30 days of purchase with a receipt.", "We accept returns within 30 days as long as you have the receipt."],
    "product_availability": ["Could you specify the product you're looking for?", "We carry a wide range of products. Please provide the product name or category."],
    "goodbye": ["Thank you for visiting! Have a great day!", "Goodbye! Feel free to reach out if you need any help again."],
    "default": ["I'm sorry, I didn't understand that. Could you please rephrase?"]
}

# Function to get response based on user's input
def get_response(user_input):
    user_input = user_input.lower()
    
    # Basic keyword matching for responses
    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])
    elif "store hours" in user_input or "open" in user_input:
        return random.choice(responses["store_hours"])
    elif "return policy" in user_input or "return" in user_input:
        return random.choice(responses["return_policy"])
    elif "available" in user_input or "have" in user_input:
        return random.choice(responses["product_availability"])
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(responses["goodbye"])
    else:
        return random.choice(responses["default"])

# Simple chatbot loop
def chat():
    print("Chatbot: Hello! Welcome to our customer service. Type 'bye' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot:", random.choice(responses["goodbye"]))
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
chat()
