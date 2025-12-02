# AI Dungeon Master

A text-based fantasy RPG adventure powered by AI. Play an immersive Dungeons & Dragons style game where the AI acts as your Dungeon Master, creating dynamic stories based on your choices.

## Features

- **Mature Fantasy RPG**: Experience dark fantasy with violence, romance, moral complexity, and real consequences
- **Dynamic Storytelling**: The AI adapts to your choices and creates unique narratives
- **Multiple Versions**:
  - **Cloud Version** (`dungeon_master.py`): Fast responses using Groq's free API (Llama 3.3 70B)
  - **Local Version** (`dungeon_master_local.py`): Complete privacy with Ollama (Qwen 2.5 14B)
- **Conversation Memory**: The AI remembers your entire adventure
- **Restart Anytime**: Type 'restart' to begin a new adventure

## Installation Methods

### Method 1: Double-Click Launcher (Mac Only - Easiest)

1. Clone this repository
2. Install Ollama and download the model:
   ```bash
   brew install ollama
   ollama pull qwen2.5:14b
   ```
3. Double-click `launch_dungeon_master.command` to play!

### Method 2: Standalone Executable (Mac - No Python Required)

1. Download the latest release from the [Releases page](https://github.com/omervaner/ai-dungeon-master/releases)
2. Extract and run `AI-Dungeon-Master` executable in Terminal
3. Make sure Ollama is installed and the model is downloaded

## Quick Start

### Option 1: Cloud Version (Recommended for Speed)

1. Clone this repository
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Get a free API key from [Groq](https://console.groq.com/)
4. Create a `.env` file:
   ```
   GROQ_API_KEY=your_api_key_here
   ```
5. Run the game:
   ```bash
   python3 dungeon_master.py
   ```

### Option 2: Local Version (Complete Privacy)

1. Install [Ollama](https://ollama.ai/)
2. Download the Qwen 2.5 14B model:
   ```bash
   ollama pull qwen2.5:14b
   ```
3. Run the game:
   ```bash
   python3 dungeon_master_local.py
   ```

## How to Play

1. The DM will ask what kind of adventure you want (fantasy quest, dungeon crawl, mystery, etc.)
2. Choose your character type (warrior, rogue, mage, cleric, etc.)
3. The AI creates your character's backstory and starting situation
4. Type your actions and the DM responds to your choices
5. Type `quit` or `exit` to end, `restart` to begin a new adventure

## Example Gameplay

```
DM: Welcome, adventurer! What kind of adventure do you seek?

You: I want to be a rogue thief in a dark fantasy city

DM: Welcome to Varakar, a grim city where danger lurks in every shadow...
[Creates your character backstory and presents options]

You: I sneak into the tavern through the back door

DM: [Describes what you find and gives you choices]
```

## Bonus: Simple Chatbot

Also includes `chatbot.py` - a basic conversational AI that remembers your conversation history. Great for learning AI integration basics!

```bash
python3 chatbot.py
```

## Tech Stack

- **Python 3.9+**
- **Groq API**: Fast cloud AI inference (free tier available)
- **Ollama**: Local AI models for privacy
- **Qwen 2.5 14B**: Powerful open-source language model
- **Llama 3.3 70B**: High-quality cloud model

## Why This Project?

This project demonstrates:
- AI API integration (Groq)
- Local AI deployment (Ollama)
- System prompts to transform chatbots into specialized applications
- Conversation history management
- Environment variable security
- Temperature settings for creative vs focused responses

## Performance Notes

- **Cloud (Groq)**: 1-2 second responses
- **Local 14B**: 10-15 second responses
- **Local 32B**: 3-5 minute responses (too slow for gameplay)

The 14B model provides the best balance of speed and quality for local gameplay.

## Contributors

Built by Omer with assistance from Claude Code for learning AI integration with Python.

## License

MIT License - Feel free to use, modify, and share!
