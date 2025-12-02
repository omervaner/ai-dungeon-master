import os
from groq import Groq
from dotenv import load_dotenv

# Load the API key from .env file
# This keeps your key secure and out of your code
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

# Create a Groq client - this is what connects to the AI
client = Groq(api_key=api_key)

print("=" * 50)
print("AI Chatbot - Powered by Groq")
print("=" * 50)
print("Type 'quit' or 'exit' to end the conversation")
print("Type 'clear' to clear conversation history\n")

# Store conversation history - this is a list of all messages
# Each message has a "role" (user or assistant) and "content" (the text)
conversation_history = []

# Main chat loop - keeps running until user quits
while True:
    # Get user input
    user_input = input("You: ")

    # Check if user wants to quit
    if user_input.lower() in ['quit', 'exit']:
        print("Goodbye!")
        break

    # Check if user wants to clear history
    if user_input.lower() == 'clear':
        conversation_history = []
        print("Conversation history cleared!\n")
        continue

    # Skip empty messages
    if not user_input.strip():
        continue

    # Add the user's message to the conversation history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    try:
        # Send the ENTIRE conversation history to Groq AI
        # This is how the AI remembers previous messages
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # The AI model we're using
            messages=conversation_history,  # Send all previous messages
            temperature=0.7,  # Controls randomness (0=focused, 2=creative)
            max_tokens=1024  # Maximum length of response
        )

        # Extract the AI's response from the API result
        ai_message = response.choices[0].message.content

        # Add the AI's response to conversation history
        conversation_history.append({
            "role": "assistant",
            "content": ai_message
        })

        # Print the AI's response
        print(f"\nAI: {ai_message}\n")

    except Exception as e:
        # If something goes wrong, show the error
        print(f"\nError: {e}\n")
