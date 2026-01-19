import os
import google.generativeai as genai

# ------------------ GEMINI CONFIG ------------------ #
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=GEMINI_API_KEY)

# ✅ IMPORTANT:
# google-generativeai==0.3.2 works BEST with this alias
MODEL_NAME = "gemini-pro"

model = genai.GenerativeModel(
    MODEL_NAME,
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

    prompt = ""

    # Add previous conversation
    if chat_history:
        for user, ai in chat_history:
            prompt += f"User: {user}\n"
            prompt += f"Assistant: {ai}\n"

    # Add current user input
    prompt += f"User: {user_input}\nAssistant:"

    # ✅ Correct call for this SDK version
    response = model.generate_content(prompt)

    return response.text.strip()
