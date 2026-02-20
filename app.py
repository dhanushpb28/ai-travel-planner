import streamlit as st

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI-Powered Travel Planner")
st.markdown("Plan your trip intelligently based on your preferences.")

st.divider()

# -------- User Input Section --------

with st.form("travel_form"):

    destination = st.text_input("Destination")

    days = st.number_input(
        "Number of Days",
        min_value=1,
        max_value=30,
        value=3
    )

    budget = st.number_input(
        "Budget (USD)",
        min_value=100,
        value=1000
    )

    interests = st.multiselect(
        "Select Your Interests",
        ["Food", "Adventure", "History", "Nightlife", "Relaxation", "Shopping"]
    )

    submitted = st.form_submit_button("Generate Itinerary")

# -------- Output Section --------

if submitted:

    if not destination:
        st.error("Please enter a destination.")
    else:
        st.success("Itinerary Generated Successfully!")

        st.subheader(f"📍 Trip to {destination}")
        st.write(f"🗓 Duration: {days} days")
        st.write(f"💰 Budget: ${budget}")
        st.write(f"🎯 Interests: {', '.join(interests) if interests else 'Not specified'}")

        st.divider()

        st.subheader("📝 Sample Itinerary")

        for day in range(1, days + 1):
            st.markdown(f"**Day {day}:** Explore major attractions and enjoy local experiences.")