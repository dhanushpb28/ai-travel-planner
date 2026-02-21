# AI-Powered Travel Planner
## Overview

AI-Powered Travel Planner is an intelligent web application that generates personalized travel itineraries based on user inputs such as destination, duration, budget, and interests.

The application integrates Google Gemini (via the official Google GenAI SDK) to dynamically generate structured, day-by-day travel plans. The system is designed to be modular and extensible, allowing integration of real-time APIs such as weather services and travel data providers.

## Features

- User input for destination, duration, budget, and interests

- AI-generated structured itinerary using Google Gemini

- Budget-aware recommendations

- Modular and scalable architecture

- Streamlit-based interactive UI


## Tech Stack

- Python 3.9+

- Streamlit

- Google GenAI SDK (google-genai)

- Gemini 3 Flash Preview Model

- Python Dotenv (for environment variable management)



## API Key Setup (Required)

This project uses Google Gemini API.

1. Go to: https://aistudio.google.com/
2. Create an API key.
3. Create a `.env` file in the project root:

    ```bash
    GEMINI_API_KEY=your_actual_api_key_here
    ```

⚠️ Do not commit your `.env` file to GitHub.


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