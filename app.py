"""
Smart CLI Chatbot
A beginner-friendly CLI-based AI chatbot using Groq's API.
Features conversation memory for contextual responses.
"""

import os
import sys
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "llama-3.1-8b-instant"
MAX_TOKENS = 150


def initialize_client():
    """
    Initialize and return Groq client.
    Handles missing API key error.
    """
    if not API_KEY:
        print("Error: OPENAI_API_KEY not found in .env file")
        print("Please add your API key to the .env file")
        sys.exit(1)

    return Groq(api_key=API_KEY)


def initialize_conversation():
    """
    Initialize conversation with a system message.
    The system message sets the AI's personality and behavior.
    """
    return [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Keep responses concise and friendly."
        }
    ]


def get_response(client, messages):
    """
    Get AI response using full conversation history.
    The messages list contains all previous exchanges.
    """
    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=0.7
        )

        return completion.choices[0].message.content

    except Exception as e:
        print(f"\nError: {e}")
        return None


def add_messages(messages, role, content):
    """
    Add a message to the conversation history.
    Role can be 'user' or 'assistant'.
    """
    messages.append({
        "role": role,
        "content": content
    })


def print_welcome():
    """Print welcome message and instructions."""
    print("=" * 50)
    print("       Welcome to Smart CLI Chatbot!")
    print("=" * 50)
    print("\nInstructions:")
    print("- Type your message and press Enter")
    print("- Type 'exit' to quit the chatbot")
    print("- Chat history is maintained for context")
    print("-" * 50)


def main():
    """
    Main function to run the chatbot.
    Maintains conversation memory throughout the session.
    """
    client = initialize_client()
    messages = initialize_conversation()
    print_welcome()

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                print("Please enter a message.")
                continue

            if user_input.lower() == "exit":
                print("\nGoodbye! Have a great day!")
                break

            add_messages(messages, "user", user_input)

            print("\nAI: ", end="", flush=True)

            response = get_response(client, messages)

            if response:
                print(response)
                add_messages(messages, "assistant", response)
            else:
                print("Sorry, I couldn't get a response. Please try again.")
                messages.pop()

        except KeyboardInterrupt:
            print("\n\nChatbot interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\nInput ended. Goodbye!")
            break


if __name__ == "__main__":
    main()