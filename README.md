# 🤖 ByteBuddy AI Chatbot

**ByteBuddy AI** is a powerful, modern AI chatbot built using **Python**, **Streamlit**, and **Google Gemini API**.  
It supports **AI chat**, **document-based question answering**, and **voice interaction**, all in one interactive web app.

🌐 **Live App:** https://bytebuddy-ai-chatbot.streamlit.app/

---

## 🚀 Features

- **💬 AI Chat**
  - Ask any question in natural language
  - Context-aware conversation using chat memory
  - Powered by Google Gemini models

- **📄 Document Question Answering**
  - Upload **PDF**, **DOCX**, or **TXT** files
  - Ask questions directly from documents
  - Smart summarization and extraction

- **🎤 Voice Assistant**
  - Speak instead of typing
  - Converts voice to text
  - AI responds intelligently

- **🌗 Light / Dark Theme**
  - Toggle between **Day mode** and **Night mode**
  - Modern animated UI

- **🧠 Chat Memory**
  - Maintains conversation context
  - Clear chat anytime

---

## 🛠️ Tech Stack

- **Frontend**
  - Streamlit
  - Custom HTML & CSS
  - Animations & responsive layout

- **Backend**
  - Python
  - Google Gemini API
  - Document parsing logic

- **AI Models**
  - Gemini Flash / Pro models
  - Gemini Embeddings

---

## 📁 Project Structure

ByteBuddy-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── chatbot/
│ ├── gemini_chat.py
│ ├── chat_memory.py
│ └── voice_input.py
│
├── document_qa/
│ └── doc_chat.py
│
└── assets/


---

## 🔑 Gemini API Setup

1. Go to **Google AI Studio**
2. Create a **Gemini API Key**
3. In Streamlit Cloud:
   - Go to **App Settings → Secrets**
   - Add:
     ```md
     GEMINI_API_KEY = "your_api_key_here"
     ```

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Manu082/ByteBuddy-AI-Chatbot.git
cd ByteBuddy-AI-Chatbot

### 2️⃣ Create Virtual Environment 
```bash
  python -m venv venv


