import streamlit as st
import os

# 🔥 ADDITION 1: Gemini import
from chatbot.gemini_chat import ask_gemini

# 🔥 ADDITION 5: Document Q&A import
from document_qa.doc_chat import document_question_answer

# 🔥 ADDITION 7: Chat memory + Voice input imports
from chatbot.chat_memory import (
    init_chat_memory,
    add_to_chat,
    get_chat_history,
    clear_chat
)

from chatbot.voice_input import listen_from_mic

# ------------------ BASIC CONFIG ------------------ #
st.set_page_config(
    page_title="ByteBuddy AI – Smart Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# 🔥 ADDITION 8: Initialize centralized chat memory
init_chat_memory()

# 🔥 ADDITION 6: Document history
if "doc_history" not in st.session_state:
    st.session_state.doc_history = []

# ================== CHANGE 1: DAY / NIGHT THEME ================== #
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

if st.session_state.theme == "dark":
    BG_GRADIENT = "linear-gradient(135deg, #0f2027, #203a43, #2c5364)"
    TEXT_COLOR = "white"
else:
    BG_GRADIENT = "linear-gradient(135deg, #f8fafc, #e2e8f0)"
    TEXT_COLOR = "#020617"

# ------------------ CUSTOM CSS (ANIMATION + UI) ------------------ #
st.markdown(f"""
<style>

/* Main background */
.stApp {{
    background: {BG_GRADIENT};
    color: {TEXT_COLOR};
    transition: all 0.4s ease;
}}

/* Title animation */
@keyframes glow {{
    0% {{ text-shadow: 0 0 5px #00f2ff; }}
    50% {{ text-shadow: 0 0 20px #00f2ff; }}
    100% {{ text-shadow: 0 0 5px #00f2ff; }}
}}

.main-title {{
    font-size: 48px;
    font-weight: 800;
    text-align: center;
    animation: glow 2s infinite;
}}

/* Chat bubble */
.chat-box {{
    background: rgba(255,255,255,0.10);
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}}

/* Buttons */
.stButton > button {{
    background: linear-gradient(90deg, #00f2ff, #4facfe);
    color: black;
    font-weight: bold;
    border-radius: 25px;
    padding: 10px 22px;
    border: none;
}}

.stButton > button:hover {{
    transform: scale(1.07);
}}

/* Sidebar */
.css-1d391kg {{
    background: rgba(0,0,0,0.4);
}}

</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------ #
st.markdown('<div class="main-title">🤖 ByteBuddy AI</div>', unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:18px;'>"
    "Your Personal AI Assistant for Chat, Documents & Voice Commands"
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# ------------------ SIDEBAR ------------------ #
st.sidebar.title("⚙️ ByteBuddy Controls")

st.sidebar.button("🌞 / 🌙 Toggle Theme", on_click=toggle_theme)

mode = st.sidebar.radio(
    "Select Mode",
    ["💬 AI Chat", "📄 Document Q&A", "🎤 Voice Assistant"]
)

st.sidebar.markdown("---")

# 🔥 ADDITION 9: Clear chat button
if st.sidebar.button("🗑 Clear Chat"):
    clear_chat()
    st.session_state.doc_history = []

st.sidebar.info(
    "💡 **Powered by Gemini API**\n\n"
    "• Ask anything\n"
    "• Upload PDF / DOCX / TXT\n"
    "• Voice commands supported"
)

# ------------------ MAIN CONTENT ------------------ #
if mode == "💬 AI Chat":
    st.subheader("💬 Chat with ByteBuddy")

    user_input = st.text_input(
        "Type your question here 👇",
        placeholder="e.g. What is Python and where is it used?"
    )

    if st.button("Ask AI"):
        if user_input.strip() == "":
            st.warning("⚠️ Please type a question.")
        else:
            with st.spinner("🤖 ByteBuddy is thinking..."):
                st.markdown(
                    f"<div class='chat-box'><b>You:</b> {user_input}</div>",
                    unsafe_allow_html=True
                )

                response = ask_gemini(
                    user_input,
                    get_chat_history()
                )

                add_to_chat(user_input, response)

                st.markdown(
                    f"<div class='chat-box'><b>ByteBuddy:</b> {response}</div>",
                    unsafe_allow_html=True
                )

    if get_chat_history():
        st.markdown("### 💬 Conversation History")
        for user, ai in get_chat_history()[::-1]:
            st.markdown(
                f"<div class='chat-box'><b>You:</b> {user}</div>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<div class='chat-box'><b>ByteBuddy:</b> {ai}</div>",
                unsafe_allow_html=True
            )

elif mode == "📄 Document Q&A":
    st.subheader("📄 Ask Questions from Documents")

    uploaded_file = st.file_uploader(
        "Upload PDF / DOCX / TXT",
        type=["pdf", "docx", "txt"]
    )

    question = st.text_input(
        "Ask a question from the document",
        placeholder="e.g. Summarize this document"
    )

    if st.button("Ask from Document"):
        if uploaded_file is None:
            st.warning("⚠️ Please upload a document.")
        elif question.strip() == "":
            st.warning("⚠️ Please ask a question.")
        else:
            with st.spinner("📚 Analyzing document with ByteBuddy..."):
                answer = document_question_answer(uploaded_file, question)

                st.session_state.doc_history.append((question, answer))

                st.markdown(
                    f"<div class='chat-box'><b>Question:</b> {question}</div>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"<div class='chat-box'><b>ByteBuddy:</b> {answer}</div>",
                    unsafe_allow_html=True
                )

    if st.session_state.doc_history:
        st.markdown("### 📄 Document Q&A History")
        for q, a in st.session_state.doc_history[::-1]:
            st.markdown(
                f"<div class='chat-box'><b>Question:</b> {q}</div>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<div class='chat-box'><b>ByteBuddy:</b> {a}</div>",
                unsafe_allow_html=True
            )

elif mode == "🎤 Voice Assistant":
    st.subheader("🎤 Voice Assistant")

    st.info(
        "🎙️ Click the button and speak.\n\n"
        "ByteBuddy will understand your voice and respond."
    )

    if st.button("🎤 Start Listening"):
        with st.spinner("🎧 Listening..."):
            voice_text = listen_from_mic()

        st.markdown(
            f"<div class='chat-box'><b>You (Voice):</b> {voice_text}</div>",
            unsafe_allow_html=True
        )

        if not voice_text.startswith("⚠️") and not voice_text.startswith("❌"):
            with st.spinner("🤖 ByteBuddy is thinking..."):
                response = ask_gemini(
                    voice_text,
                    get_chat_history()
                )

                add_to_chat(voice_text, response)

                st.markdown(
                    f"<div class='chat-box'><b>ByteBuddy:</b> {response}</div>",
                    unsafe_allow_html=True
                )

# ------------------ FOOTER ------------------ #
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:14px;'>"
    "© 2026 ByteBuddy AI | Built by Manas Didwania 🚀"
    "</p>",
    unsafe_allow_html=True
)
