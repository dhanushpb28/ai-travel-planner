import streamlit as st
from ai_engine import generate_chat_response

st.set_page_config(
    page_title="AI Travel Assistant",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Travel Assistant")
st.markdown("Chat with your personal AI travel planner.")
st.markdown("---")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! 👋 Where would you like to travel?"
        }
    ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Tell me your travel plans...")

if user_input:

    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Planning your trip... ✈️"):
            response = generate_chat_response(st.session_state.messages)
            st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )