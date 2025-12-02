import os
from groq import Groq
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

# Create a Groq client
client = Groq(api_key=api_key)

print("=" * 60)
print("AI DUNGEON MASTER")
print("=" * 60)
print("A text-based adventure powered by AI")
print("Type 'quit' or 'exit' to end your adventure")
print("Type 'restart' to start a new adventure\n")

# THE MAGIC: System prompt that tells the AI to be a Dungeon Master
# This is what transforms a chatbot into a game!
SYSTEM_PROMPT = """You are an expert Dungeon Master running a fantasy RPG adventure.

RULES:
- Create vivid, immersive descriptions of locations, characters, and events
- Let the player make choices and respond to whatever they decide to do
- Keep track of the story, locations visited, NPCs met, and items collected
- Add danger, mystery, and excitement to the adventure
- When combat happens, describe it narratively and determine outcomes based on player actions
- Be creative and adaptive - if the player tries something unexpected, roll with it
- Keep responses focused and engaging (2-4 paragraphs max)
- End each response by presenting the player with their current situation and options

Start by asking the player what kind of adventure they want (fantasy quest, dungeon crawl, mystery, etc.) and what kind of character they want to be."""

# Store conversation history with the system prompt at the start
conversation_history = [
    {
        "role": "system",  # System role tells the AI how to behave
        "content": SYSTEM_PROMPT
    }
]

# Send initial message to start the game
print("DM: Welcome, adventurer!\n")
try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history,
        temperature=0.9,  # Higher = more creative and unpredictable (perfect for storytelling)
        max_tokens=1024
    )

    dm_message = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": dm_message
    })

    print(f"DM: {dm_message}\n")
    print("-" * 60 + "\n")

except Exception as e:
    print(f"Error starting game: {e}")
    exit()

# Main game loop
while True:
    # Get player input
    player_action = input("You: ")

    # Check if player wants to quit
    if player_action.lower() in ['quit', 'exit']:
        print("\nThanks for playing! Your adventure ends here.")
        break

    # Check if player wants to restart
    if player_action.lower() == 'restart':
        # Reset conversation but keep the system prompt
        conversation_history = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]
        print("\nStarting a new adventure...\n")
        continue

    # Skip empty messages
    if not player_action.strip():
        continue

    # Add player's action to conversation history
    conversation_history.append({
        "role": "user",
        "content": player_action
    })

    try:
        # Send to AI and get DM response
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=conversation_history,
            temperature=0.9,
            max_tokens=1024
        )

        dm_message = response.choices[0].message.content

        # Add DM response to history
        conversation_history.append({
            "role": "assistant",
            "content": dm_message
        })

        # Print the DM's response
        print(f"\nDM: {dm_message}\n")
        print("-" * 60 + "\n")

    except Exception as e:
        print(f"\nError: {e}\n")
