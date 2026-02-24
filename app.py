import streamlit as st
from ai_engine import generate_chat_response
import random
import uuid
import time

st.set_page_config(
    page_title="AI Travel Assistant",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Travel Assistant")
st.markdown("Chat with your personal travel planner.")
st.markdown("---")

# ---------------------------
# Session Initialization
# ---------------------------
if "sessions" not in st.session_state:
    st.session_state.sessions = {}

if "current_session" not in st.session_state:
    session_id = str(uuid.uuid4())
    st.session_state.sessions[session_id] = {
        "title": "New Chat",
        "messages": [
            {
                "role": "assistant",
                "content": "Hi! 👋 I’m your travel assistant. Where would you like to go?"
            }
        ]
    }
    st.session_state.current_session = session_id

# ---------------------------
# Sidebar (ChatGPT Style)
# ---------------------------
with st.sidebar:
    st.markdown("## 💬 Chat Sessions")

    if st.button("➕ New Chat"):
        session_id = str(uuid.uuid4())
        st.session_state.sessions[session_id] = {
            "title": "New Chat",
            "messages": [
                {
                    "role": "assistant",
                    "content": "Hi! 👋 I’m your travel assistant. Where would you like to go?"
                }
            ]
        }
        st.session_state.current_session = session_id
        st.rerun()

    st.markdown("---")

    for session_id, session_data in st.session_state.sessions.items():

        is_active = session_id == st.session_state.current_session
        title = session_data["title"]

        col1, col2, col3 = st.columns([6,1,1])

        # Highlight active session
        button_style = "primary" if is_active else "secondary"

        if col1.button(title, key=f"switch_{session_id}", type=button_style):
            st.session_state.current_session = session_id
            st.rerun()

        # Rename
        if col2.button("✏️", key=f"rename_{session_id}"):
            new_name = st.text_input(
                "Rename chat:",
                value=title,
                key=f"input_{session_id}"
            )
            if new_name:
                st.session_state.sessions[session_id]["title"] = new_name

        # Delete
        if col3.button("🗑", key=f"delete_{session_id}"):
            del st.session_state.sessions[session_id]
            if session_id == st.session_state.current_session:
                new_id = str(uuid.uuid4())
                st.session_state.sessions[new_id] = {
                    "title": "New Chat",
                    "messages": [
                        {
                            "role": "assistant",
                            "content": "Hi! 👋 I’m your travel assistant. Where would you like to go?"
                        }
                    ]
                }
                st.session_state.current_session = new_id
            st.rerun()

# ---------------------------
# Load Current Session
# ---------------------------
current_session = st.session_state.current_session
messages = st.session_state.sessions[current_session]["messages"]

# Display chat history
for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------
# User Input
# ---------------------------
user_input = st.chat_input("Tell me about your travel plans...")

if user_input:

    # Auto-rename on first user message
    if st.session_state.sessions[current_session]["title"] == "New Chat":
        st.session_state.sessions[current_session]["title"] = user_input[:40]

    messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        loading_messages = [
            "Scanning destinations... 🌍",
            "Designing your personalized travel plan...",
            "Analyzing your travel preferences... ✈️",
            "Crafting your perfect itinerary... 🗺",
            "Preparing your travel experience... ✨",
            "Planning your perfect getaway…",
            "Charting your travel route…",
            "Discovering the best places for you…"
        ]

        with st.spinner(random.choice(loading_messages)):
            response = generate_chat_response(messages)

        placeholder = st.empty()
        full_response = ""

        for char in response:
            full_response += char
            placeholder.markdown(full_response)
            time.sleep(0.003)

    messages.append({"role": "assistant", "content": response})