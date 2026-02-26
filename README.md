# Explore-with-AI-Custom-Itineraries-for-Your-Next-Journey


An AI-powered **Travel Itinerary Generator** built with **Python, Streamlit, and Google Gemini API**.  
This app creates personalized travel itineraries based on your destination, trip duration, and travel style.

---

## ✨ Features
- 🏖️ Generates day-wise itineraries (Morning, Afternoon, Evening)
- 🧳 Supports multiple travel styles: Adventure, Relaxation, Cultural, Spiritual
- 💡 Adds travel tips for each day
- 🎨 Styled UI with dark theme and custom CSS
- 🔒 Secure API key handling using environment variables

---

## 📂 Project Structure
 Genai_travel_project/
- GENAI/
  - travel.py
  - requirements.txt
  - .streamlit/
- Documentation/
- README.md


## ⚙️ Installation & Setup
1. Clone the repository:
  https://github.com/Nallamachkeerthi/Explore-with-AI-Custom-Itineraries-for-Your-Next-Journey


2. Create and activate a virtual environment:
   python -m venv myenv
   .\myenv\Scripts\activate
 

3. Install dependencies:
   pip install -r requirements.txt
  

4. Set your Gemini API key (Windows PowerShell):
   setx GEMINI_API_KEY "your_actual_api_key_here"
   

5. Run the app:
   streamlit run travel.py

---

## 🎥 Demo Video
https://drive.google.com/file/d/10tZrE6RRcV1gEa-OIAEceNKZpaq11MGz/view?usp=sharing

---

## 🛡️ Security Note
- API keys are **never hardcoded** in the code.  
- Keys are stored securely in environment variables.  

---

## 📜 License
This project is licensed under the MIT License.
```
## requirements.txt
streamlit
google-generativeai

