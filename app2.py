import streamlit as st
import nltk
from transformers import pipeline

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load AI model for automatic text generation
chatbot = pipeline("text-generation", model="distilgpt2", max_length=500)

# Medicine and diet suggestions
medicines = {
    "fever": "💊 **Paracetamol (Crocin, Dolo 650)** - Take as prescribed.",
    "headache": "💊 **Aspirin or Ibuprofen** - Helps relieve pain.",
    "stomach pain": "💊 **Antacids (Gelusil, Digene)** - Reduces acidity & pain.",
    "cold": "💊 **Antihistamines (Cetirizine, Allegra)** - Helps with congestion.",
    "cough": "💊 **Cough Syrup (Benadryl, Honitus)** - Soothes throat.",
    "bleeding": "💊 **Apply antiseptic & use sterile bandages** - Seek medical help if severe."
}

healthy_diets = [
    "🥗 **Balanced Diet**: Vegetables, lean proteins, whole grains & fruits.",
    "🍎 **Immunity Boosting**: Citrus fruits, turmeric milk, green tea, nuts.",
    "💪 **Protein Rich**: Eggs, chicken, lentils, fish, and dairy."
]

def healthcare_chatbot(user_input):
    # Check if user input matches medicine keywords
    for key in medicines:
        if key in user_input.lower():
            return medicines[key]

    # Check if user asks for a diet suggestion
    if "diet" in user_input.lower() or "nutrition" in user_input.lower():
        return "🍽 **Healthy Diet Suggestion:** " + healthy_diets[0]

    # Otherwise, generate an AI response
    response = chatbot(user_input, max_length=500, num_return_sequences=1)
    return response[0]["generated_text"]

def main():
    st.set_page_config(page_title="Healthcare Assistant Chatbot", layout="wide")

    # Title with icon
    st.markdown("<h1 style='text-align: center; color: #48DDAC;'>🩺 AI Healthcare Assistant</h1>", unsafe_allow_html=True)

    # User input section
    user_input = st.text_input("💬 **How can I assist you today?**", placeholder="E.g., What should I take for a fever?")

    if st.button("🚀 Submit"):
        if user_input:
            st.markdown(f"<b style='color: blue;'>👤 You:</b> {user_input}", unsafe_allow_html=True)
            with st.spinner("🔄 Processing your query..."):
                response = healthcare_chatbot(user_input)

            # Highlighted AI response box with a sleek style
            st.markdown(
                f"""
                <div style="
                    background-color: #2E3B4E;
                    padding: 12px;
                    border-radius: 10px;
                    margin-top: 10px;
                    color: #E6E6E6;
                    font-weight: bold;
                    font-size: 16px;
                ">
                    🤖 <b>AI Assistant:</b> {response}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning("⚠️ **Please enter a valid query.**")

    st.markdown("<h4 style='text-align: center; color: grey;'>💡 Health Advice, Anytime</h4>", unsafe_allow_html=True)
main()


