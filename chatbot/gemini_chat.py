# chatbot/gemini_chat.py

import streamlit as st
import google.generativeai as genai

# ✅ Read API key from Streamlit secrets
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in Streamlit secrets")

# ✅ Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Use supported Gemini model
MODEL_NAME = "models/gemini-1.5-flash"

def ask_gemini(user_input, chat_history=None):
    try:
        model = genai.GenerativeModel(MODEL_NAME)

        # Build prompt with last 5 messages
        prompt = user_input
        if chat_history:
            history_text = "\n".join(
                [f"User: {u}\nAI: {a}" for u, a in chat_history[-5:]]
            )
            prompt = history_text + "\nUser: " + user_input

        response = model.generate_content(prompt)

        return response.text.strip() if response.text else "⚠️ No response from Gemini."

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"
