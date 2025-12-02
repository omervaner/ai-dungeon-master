import requests
import json

# Ollama runs locally on your machine at this address
OLLAMA_API_URL = "http://localhost:11434/api/chat"

print("=" * 60)
print("AI DUNGEON MASTER (LOCAL)")
print("=" * 60)
print("A text-based adventure powered by LOCAL AI (Qwen 2.5 14B)")
print("Type 'quit' or 'exit' to end your adventure")
print("Type 'restart' to start a new adventure\n")

# THE MAGIC: System prompt that tells the AI to be a Dungeon Master
SYSTEM_PROMPT = """You are an expert Dungeon Master running a mature fantasy RPG adventure.

RULES:
- Create vivid, immersive descriptions of locations, characters, and events
- Let the player make choices and respond to whatever they decide to do
- Keep track of the story, locations visited, NPCs met, and items collected
- Add danger, mystery, romance, and excitement to the adventure
- When combat happens, describe it narratively with appropriate violence and consequences
- Be creative and adaptive - if the player tries something unexpected, roll with it
- Keep responses focused and engaging (2-4 paragraphs max)
- Handle mature themes appropriately (violence, romance, moral complexity)
- End each response by presenting the player with their current situation and options

This is a mature RPG where actions have real consequences. Don't shy away from dark themes, but keep them narratively appropriate.

Start by asking the player what kind of adventure they want (fantasy quest, dungeon crawl, mystery, etc.) and what kind of character they want to be."""

# Store conversation history with the system prompt
conversation_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

def chat_with_ollama(messages):
    """Send messages to Ollama and get a response"""
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": "qwen2.5:14b",  # Using Qwen 2.5 14B
                "messages": messages,
                "stream": False,  # Get full response at once
                "options": {
                    "temperature": 0.9,  # High creativity for storytelling
                    "num_ctx": 32768  # Large context window for long adventures
                }
            },
            timeout=300  # 5 minute timeout for responses (longer for detailed storytelling)
        )

        if response.status_code == 200:
            return response.json()["message"]["content"]
        else:
            return f"Error: API returned status {response.status_code}"

    except requests.exceptions.Timeout:
        return "Error: Request timed out. The model might be thinking too hard!"
    except Exception as e:
        return f"Error: {str(e)}"

# Send initial message to start the game
print("DM: Welcome, adventurer!\n")

initial_response = chat_with_ollama(conversation_history)
conversation_history.append({
    "role": "assistant",
    "content": initial_response
})

print(f"DM: {initial_response}\n")
print("-" * 60 + "\n")

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

    # Get DM response
    print("\n[Thinking...]")
    dm_message = chat_with_ollama(conversation_history)

    # Add DM response to history
    conversation_history.append({
        "role": "assistant",
        "content": dm_message
    })

    # Print the DM's response
    print(f"\nDM: {dm_message}\n")
    print("-" * 60 + "\n")
