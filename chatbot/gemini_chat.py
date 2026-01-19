# chatbot/gemini_chat.py

import streamlit as st
import google.generativeai as genai

# Read API key from Streamlit secrets
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

# ✅ FINAL, SAFE MODEL
MODEL_NAME = "models/gemini-flash-latest"

def ask_gemini(user_input, chat_history=None):
    try:
        model = genai.GenerativeModel(MODEL_NAME)

        prompt = user_input
        if chat_history:
            history_text = "\n".join(
                [f"User: {u}\nAI: {a}" for u, a in chat_history[-5:]]
            )
            prompt = history_text + "\nUser: " + user_input

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"
