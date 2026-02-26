import os
import streamlit as st
import google.generativeai as genai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🌍 Explore AI Journeys",
    layout="centered"
)

# ---------------- GOOGLE GEMINI API ----------------
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Define generation configuration
generation_config = {
    "temperature": 0.4,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background-color: #000000; /* Black background */
    color: #FFFFFF; /* White text */
}
h1, h2, h3, h4, h5, h6, p, span, label, div {
    color: #FFFFFF !important;
    opacity: 1 !important;
}
input, textarea {
    background-color: #1E1E1E !important;
    color: #FFFFFF !important;
}
button {
    background-color: transparent !important;
    border: 1px solid #00BFFF !important; /* Blue button border */
    color: #00BFFF !important;
}
.output-box {
    border: 1px solid #00BFFF;
    padding: 20px;
    border-radius: 10px;
    background-color: #0E1117;
    color: #FFFFFF;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>🌍 Explore AI Journeys</h1>", unsafe_allow_html=True)

# ---------------- INPUTS ----------------
destination = st.text_input("Enter your desired destination:")
days = st.number_input("Enter the number of days:", min_value=1, step=1)
nights = st.number_input("Enter the number of nights:", min_value=0, step=1)
travel_style = st.selectbox("Choose your travel style:", ["Adventure", "Relaxation", "Cultural", "Spiritual"])

# ---------------- BUTTON ----------------
if st.button("Generate Itinerary"):
    if destination.strip() == "":
        st.error("Please enter a destination")
    else:
        with st.spinner("Generating itinerary..."):
            prompt = f"""
Create a detailed travel itinerary.

Destination: {destination}
Days: {days}
Nights: {nights}
Travel Style: {travel_style}

FORMAT:
- Title
- Short introduction
- Day-wise itinerary (Morning, Afternoon, Evening)
- Important Notes section
- Add one travel tip each day
"""
            response = model.generate_content(prompt, generation_config=generation_config)

            st.markdown("### Generated Itinerary")
            st.markdown(
                f"<div class='output-box'>{response.text.replace(chr(10), '<br>')}</div>",
                unsafe_allow_html=True
            )


