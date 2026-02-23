import streamlit as st
from ai_engine import generate_chat_response
import random
st.set_page_config(
    page_title="AI Travel Assistant",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Travel Assistant")
st.markdown("Chat with your personal travel planner.")
st.markdown("---")

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! 👋 I’m your travel assistant. Where would you like to go?"
        }
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Tell me about your travel plans...")

if user_input:

    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

       # 3️⃣ Generate assistant response  ← PASTE SPINNER HERE
    with st.chat_message("assistant"):

        loading_messages = [
            "Scanning destinations... 🌍",
            "Designing your personalized travel plan... ",
            "Analyzing your travel preferences... ✈️",
            "Crafting your perfect itinerary... 🗺",
            "Preparing your travel experience... ✨",
            "Designing your perfect itinerary... 🗺",
            "Planning your perfect getaway…",
            "Charting your travel route…",
            "Discovering the best places for you…"
        ]

        with st.spinner(random.choice(loading_messages)):
            response = generate_chat_response(st.session_state.messages)
            st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )