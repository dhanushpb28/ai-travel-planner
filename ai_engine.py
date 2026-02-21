import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

PRIMARY_MODEL = "gemini-3-flash-preview"


def generate_itinerary(from_city, to_city, start_date, end_date, days, people, budget, interests):

    interests_text = ", ".join(interests) if interests else "general tourism"

    per_person_budget = budget // people

    prompt = f"""
    Create a detailed travel itinerary:

    Departure City: {from_city}
    Destination: {to_city}
    Travel Dates: {start_date} to {end_date}
    Duration: {days} days
    Number of Travelers: {people}
    Total Budget: ₹{budget} INR
    Approx Budget Per Person: ₹{per_person_budget} INR
    Interests: {interests_text}

    Include:
    - Suggested travel option (flight/train) with approximate INR cost
    - Accommodation recommendation (based on group size)
    - Day-by-day plan (morning, afternoon, evening)
    - Local food or beverages to try
    - Estimated daily budget breakdown in INR

    Format clearly day by day.
    """

    try:
        response = client.models.generate_content(
            model=PRIMARY_MODEL,
            contents=prompt,
        )
        return response.text

    except Exception as e:
        time.sleep(2)
        return f"API temporarily unavailable. Please try again.\n\nError: {str(e)}"