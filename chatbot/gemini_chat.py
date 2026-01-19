import google.generativeai as genai
import os
from dotenv import load_dotenv

# ------------------ LOAD ENV ------------------ #
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

# ------------------ CONFIGURE GEMINI ------------------ #
genai.configure(api_key=API_KEY)

# ✅ FREE-TIER SAFE MODEL
MODEL_NAME = "models/gemini-flash-lite-latest"
model = genai.GenerativeModel(MODEL_NAME)

print(f"✅ ByteBuddy using model: {MODEL_NAME}")

# ------------------ MAIN CHAT FUNCTION ------------------ #
def ask_gemini(user_prompt, chat_history=None):
    context = ""
    if chat_history:
        for user, ai in chat_history:
            context += f"User: {user}\nAI: {ai}\n"

    prompt = f"""
You are ByteBuddy AI, a smart, friendly, and professional assistant.

Conversation so far:
{context}

User question:
{user_prompt}
"""

    response = model.generate_content(prompt)
    return response.text.strip()
