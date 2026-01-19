import os
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in Streamlit Secrets")

genai.configure(api_key=API_KEY)

MODEL_NAME = "models/gemini-flash-lite-latest"
model = genai.GenerativeModel(MODEL_NAME)

def ask_gemini(user_prompt, chat_history=None):
    context = ""
    if chat_history:
        for u, a in chat_history:
            context += f"User: {u}\nAI: {a}\n"

    prompt = f"""
You are ByteBuddy AI, a helpful assistant.

Conversation so far:
{context}

User:
{user_prompt}
"""
    response = model.generate_content(prompt)
    return response.text.strip()
