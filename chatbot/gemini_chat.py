import os
import google.generativeai as genai

# ------------------ GEMINI CONFIG ------------------ #
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=GEMINI_API_KEY)

# ✅ USE STABLE, CLOUD-SAFE MODEL
MODEL_NAME = "models/gemini-pro-latest"

model = genai.GenerativeModel(
    model_name=MODEL_NAME,
    generation_config={
        "temperature": 0.7,
        "top_p": 0.9,
        "max_output_tokens": 1024
    }
)

# ------------------ CHAT FUNCTION ------------------ #
def ask_gemini(user_input, chat_history=None):
    """
    user_input: str
    chat_history: list of (user, ai) tuples
    """

    contents = []

    # ✅ Add conversation history (CORRECT FORMAT)
    if chat_history:
        for user, ai in chat_history:
            contents.append({
                "role": "user",
                "parts": [{"text": user}]
            })
            contents.append({
                "role": "model",
                "parts": [{"text": ai}]
            })

    # ✅ Add current user message
    contents.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    # ✅ Correct request format for Gemini 2.x+
    response = model.generate_content(
        contents=contents
    )

    return response.text.strip()
