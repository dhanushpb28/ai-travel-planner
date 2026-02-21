import streamlit as st
from datetime import date
from ai_engine import generate_itinerary

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI-Powered Travel Planner")
st.markdown("Plan your trip intelligently based on your preferences.")
st.markdown("---")

# ---------- Input Form ----------
with st.form("travel_form"):

    col1, col2 = st.columns(2)

    with col1:
        from_city = st.text_input("🛫 From (Departure City)")
        to_city = st.text_input("🛬 To (Destination City)")

    with col2:
        start_date = st.date_input("📅 Start Date", min_value=date.today())
        end_date = st.date_input("📅 End Date", min_value=date.today())

    people = st.number_input(
        "👥 Number of Travelers",
        min_value=1,
        value=1
    )

    budget = st.number_input(
        "💰 Total Budget (INR)",
        min_value=1000,
        value=50000
    )

    interests = st.multiselect(
        "🎯 Select Your Interests",
        ["Food", "Adventure", "History", "Nightlife", "Relaxation", "Shopping"]
    )

    submitted = st.form_submit_button("✨ Generate Itinerary")

# ---------- Output ----------
if submitted:

    if not from_city or not to_city:
        st.error("Please enter both departure and destination cities.")
    elif end_date <= start_date:
        st.error("End date must be after start date.")
    else:
        try:
            total_days = (end_date - start_date).days

            st.info("Generating AI-powered itinerary... Please wait ⏳")

            itinerary = generate_itinerary(
                from_city,
                to_city,
                start_date,
                end_date,
                total_days,
                people,
                budget,
                interests
            )

            st.markdown("---")
            st.subheader("📝 Your AI-Generated Itinerary")
            st.write(itinerary)

        except Exception as e:
            st.error("Something went wrong while generating the itinerary.")
            st.write(str(e))