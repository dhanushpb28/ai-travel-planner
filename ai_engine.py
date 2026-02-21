import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

def generate_itinerary(from_city, to_city, start_date, end_date, days, budget, interests):

    interests_text = ", ".join(interests) if interests else "general tourism"

    prompt = f"""
    Create a detailed travel itinerary:

    Departure City: {from_city}
    Destination: {to_city}
    Travel Dates: {start_date} to {end_date}
    Duration: {days} days
    Budget: ${budget}
    Interests: {interests_text}

    Include:
    - Suggested travel option (flight/train)
    - Accommodation recommendation
    - Day-by-day plan (morning, afternoon, evening)
    - Local food or beverages to try
    - Estimated daily budget breakdown

    Format clearly day by day.
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text