"""
ByteBuddy AI - Chat Memory Module
--------------------------------
Handles chat memory storage and retrieval
using Streamlit session state.
"""

import streamlit as st


def init_chat_memory():
    """Initialize chat memory if not present."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def add_to_chat(user_message, ai_message):
    """Add a conversation pair to memory."""
    st.session_state.chat_history.append(
        (user_message, ai_message)
    )


def get_chat_history():
    """Return full chat history."""
    return st.session_state.chat_history


def clear_chat():
    """Clear chat memory."""
    st.session_state.chat_history = []
