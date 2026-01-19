# chatbot/gemini_chat.py

import google.generativeai as genai
from config.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "models/gemini-2.5-flash"

model = genai.GenerativeModel(MODEL_NAME)


def ask_gemini(user_input, chat_history=None):
    """
    user_input: str
    chat_history: list of (user, ai) tuples
    """

    contents = []

    # Add previous chat history
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

    # Add current user input
    contents.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    response = model.generate_content(
        contents=contents,
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 512
        }
    )

    return response.text
