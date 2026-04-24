# Smart CLI Chatbot

A beginner-friendly CLI-based AI chatbot with conversation memory, built with Python and Groq API.

## Features & Tech Stack

- **Language**: Python 3.8+
- **API**: Groq API (Llama 3.1 model)
- **Conversation Memory**: Remembers previous messages for contextual responses
- **Libraries**: `groq` (API client), `python-dotenv` (env variables)
- **Architecture**: CLI-based, modular functions with conversation state management

## Setup

1. **Clone and install dependencies**
   ```bash
   git clone <your-repo-url>
   cd smart-cli-chatbot
   pip install -r requirements.txt
   ```

2. **Configure API key**
   - Get your key from [Groq Console](https://console.groq.com/keys)
   - Add to `.env` file: `OPENAI_API_KEY=your_key_here`

## Usage

```bash
python app.py
```

- Type messages and press **Enter** to chat
- Type **exit** to quit

## Project Structure

```
├── app.py           # Main chatbot logic
├── .env             # API key configuration
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

## Example Session

```
==================================================
       Welcome to Smart CLI Chatbot!
==================================================

You: My name is Alice
AI: Nice to meet you, Alice!

You: What's my name?
AI: Your name is Alice!

You: exit
Goodbye!
```

## Available Models

Default: `llama-3.1-8b-instant`. Others available:
- `mixtral-8x7b-32768`
- `llama-3.1-70b-versatile`
- `llama3-70b-8192`

## License

MIT License
