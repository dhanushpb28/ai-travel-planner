# AI-Powered Travel Planner
## Overview

AI-Powered Travel Assistant is a conversational AI application that generates complete, end-to-end travel itineraries through an interactive chat interface.

The system collects trip details progressively (departure city, destination, travel dates, budget, interests, group type, number of travelers) and generates a fully structured itinerary including attractions, travel recommendations, accommodation suggestions, daily plans, food recommendations, and budget breakdown.

The assistant is powered by Google Gemini (Gemini 3 Flash Preview) via the official Google GenAI SDK and features a modern Streamlit-based chat interface with session management and streaming responses.

<br>


## Features

- Conversational AI travel assistant powered by Google Gemini
- Structured itinerary generation 
- 5 must-visit attractions
- Travel recommendation with pricing tiers (budget, standard, premium)
- Accommodation suggestions
- Detailed day-by-day itinerary
- Local food & beverage recommendations
- Estimated budget breakdown
- Multi-session chat management (ChatGPT-style sidebar)
- Streaming typing effect for realistic AI responses

<br>


## Tech Stack

- Python 3.9+

- Streamlit

- Google GenAI SDK (google-genai)

- Gemini 3 Flash Preview Model

- Python Dotenv (for environment variable management)

<br>


## API Key Setup (Required)

This project uses Google Gemini API.

1. Go to: https://aistudio.google.com/
2. Create an API key.
3. Create a `.env` file in the project root:

    ```bash
    GEMINI_API_KEY=your_actual_api_key_here
    ```

⚠️ Do not commit your `.env` file to GitHub.

<br>


## Try It Yourself
1. Clone the Repository:
    ```sh
    git clone https://github.com/your-username/ai-travel-planner.git
    ```
2. Navigate into the Project Folder
    ```sh
    cd ai-travel-planner
    ```
3. Create Virtual Environment:
    ```sh
    python -m venv venv
    ```
4. Activate Virtual Environment:

    Windows
    ```sh
    venv\Scripts\activate
    ```
    macOS/Linux
    ```sh
    source venv/bin/activate
    ```

5. Install Dependencies:
    ```sh
    pip install -r requirements.txt
    ```
6. Run the Application:
    ```sh
    streamlit run app.py
    ```
The application will open automatically in your browser.

<br>

## How It Works

The system follows a conversational AI architecture:

### Frontend (Streamlit)

- Handles chat UI

- Manages multiple chat sessions

- Displays streaming responses

### Backend Logic (ai_engine.py)

- Loads Gemini API key securely from environment variables

- Passes full conversation history to the model

- Uses a structured system instruction to collect required travel details progressively

- Generate the itinerary only after all required data is gathered

- Support post-generation modifications (e.g., cheaper version, luxury upgrade)


### AI Reasoning

- Gemini receives:

    - System instruction

    - Full conversation history

    - It generates context-aware responses

    - Once complete information is gathered, it produces a structured itinerary

<br>


## Future Improvements

- Real-time flight API integration

- Hotel booking integration

- Weather data integration

- Persistent chat storage (database)

- Deployment to Streamlit Cloud / AWS / GCP

- Enhanced UI/UX styling

- User authentication system