import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)


def generate_chat_response(messages):
    """
    Takes full conversation history and generates AI response.
    """

    # Convert chat history to formatted conversation
    conversation = ""
    for msg in messages:
        role = msg["role"].upper()
        content = msg["content"]
        conversation += f"{role}: {content}\n"

    system_instruction = """
You are a professional AI travel assistant.

Your responsibilities:
- Ask for missing details (destination, duration, budget, interests).
- Keep conversation natural and friendly.
- Once enough information is gathered, generate a complete travel itinerary.

The itinerary must include:
1. 5 must-visit attractions (numbered list)
2. Travel recommendation
3. Accommodation suggestion
4. Day-by-day plan
5. Local food & beverages
6. Estimated budget breakdown

Be structured, clean, and readable.
Do not repeat previous responses.
"""

    prompt = system_instruction + "\n\nConversation so far:\n" + conversation

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
        )

        return response.text if response.text else "Sorry, I couldn't generate a response."

    except Exception as e:
        return f"Error generating response: {str(e)}"