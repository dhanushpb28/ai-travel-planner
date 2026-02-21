import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()  # picks up GEMINI_API_KEY automatically


def generate_itinerary(destination, days, budget, interests):

    interests_text = ", ".join(interests) if interests else "general tourism"

    prompt = f"""
    Create a detailed {days}-day travel itinerary for {destination}.
    Budget: ${budget}.
    Interests: {interests_text}.

    For each day include:
    - Morning activity
    - Afternoon activity
    - Evening activity
    - Accommodation suggestion
    - Local food or beverage to try
    - Estimated daily cost breakdown

    Format clearly day by day.
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text