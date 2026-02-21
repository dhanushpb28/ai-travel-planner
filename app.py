import streamlit as st
from ai_engine import generate_itinerary

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="centered"
)

# ---------- Header ----------
st.title("🌍 AI-Powered Travel Planner")
st.markdown("Plan your trip intelligently based on your preferences.")
st.markdown("---")

# ---------- Input Form ----------
with st.form("travel_form"):

    destination = st.text_input("📍 Destination")

    days = st.number_input(
        "🗓 Number of Days",
        min_value=1,
        max_value=30,
        value=3
    )

    budget = st.number_input(
        "💰 Budget (USD)",
        min_value=100,
        value=1000
    )

    interests = st.multiselect(
        "🎯 Select Your Interests",
        ["Food", "Adventure", "History", "Nightlife", "Relaxation", "Shopping"]
    )

    submitted = st.form_submit_button("✨ Generate Itinerary")

# ---------- Output Section ----------
if submitted:

    if not destination:
        st.error("Please enter a destination.")
    else:
        try:
            st.info("Generating AI-powered itinerary... Please wait ⏳")

            itinerary = generate_itinerary(destination, days, budget, interests)

            st.markdown("---")
            st.subheader("📝 Your AI-Generated Itinerary")

            st.write(itinerary)

        except Exception as e:
            st.error("Something went wrong while generating the itinerary.")
            st.write(str(e))