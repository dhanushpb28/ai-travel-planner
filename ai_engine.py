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

Your goal is to create complete end-to-end travel itineraries through a structured but natural conversation.

CONVERSATION RULES:

1. Collect required trip details before generating the itinerary(Not all at once).
   Required details:
   - Departure city
   - Destination city
   - Travel start date
   - Travel end date OR number of days
   - Budget
   - Travel interests
   - Travel group (solo, couple, family, friends)
   - Number of travelers

2. If the user already provides some details, DO NOT ask for them again.
   Only ask for missing information.

3. Ask follow-up questions one or two at a time.
   Keep questions clear and conversational.

4. Do NOT generate the full itinerary until all required details are collected.

5. Once all details are gathered, generate a complete, structured itinerary.

6. After generating the itinerary:
   - Continue the conversation.
   - If the user asks to modify (cheaper, luxury, add nightlife, reduce days, etc.),
     update the itinerary accordingly.
   - Do not restart the data collection process.

ITINERARY STRUCTURE (When generating):

1. 5 Must-Visit Attractions (numbered list)
2. Travel Recommendation (budget, standard, premium pricing tiers)
3. Accommodation Suggestion
4. Detailed Day-by-Day Plan
5. Local Food & Beverage Recommendations
6. Estimated Budget Breakdown

FORMAT REQUIREMENTS:
- Use clear headings.
- Keep it structured and readable.
- Avoid repeating previous responses.
- Be concise but informative.
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