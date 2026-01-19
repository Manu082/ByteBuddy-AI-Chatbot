# 🤖 ByteBuddy AI Chatbot

**ByteBuddy AI** is a powerful, modern AI chatbot built using **Python**, **Streamlit**, and **Google Gemini API**.  
It supports **AI chat**, **document-based question answering**, and **voice interaction**, all in one interactive web app.

🌐 **Live App:** [https://bytebuddy-ai-chatbot.streamlit.app/](https://bytebuddy-ai-chatbot.streamlit.app/)

---

## 🚀 Features

* **💬 AI Chat**
  * **Natural Language:** Ask any question in natural language.
  * **Context-Aware:** Conversation using chat memory to remember previous prompts.
  * **Power:** Powered by high-performance Google Gemini models.

* **📄 Document Question Answering**
  * **File Support:** Upload **PDF**, **DOCX**, or **TXT** files.
  * **Direct Query:** Ask questions directly from your uploaded documents.
  * **Summarization:** Smart summarization and key information extraction.

* **🎤 Voice Assistant**
  * **Hands-Free:** Speak your questions instead of typing.
  * **Conversion:** High-accuracy voice-to-text processing.
  * **Intelligence:** AI processes and responds to voice commands intelligently.

* **🌗 Light / Dark Theme**
  * **Customization:** Toggle between **Day mode** and **Night mode**.
  * **UI/UX:** Modern animated interface with responsive design.

* **🧠 Chat Memory**
  * **History:** Maintains conversation context throughout the session.
  * **Control:** Clear chat history anytime with a single click.

---

## 🛠️ Tech Stack

* **Frontend**
  * **Streamlit:** For the web framework.
  * **Custom HTML & CSS:** For unique styling and animations.

* **Backend**
  * **Python:** Core logic and processing.
  * **Google Gemini API:** Providing the LLM capabilities.
  * **Document Parsing:** Logic for handling various file formats.

* **AI Models**
  * **Gemini Flash / Pro:** Latest generative AI models.
  * **Gemini Embeddings:** For vector-based document search.

---

## 📁 Project Structure

```text
ByteBuddy-AI-Chatbot/
│
├── app.py                # Main application entry point
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
│
├── chatbot/              # Chat logic and modules
│   ├── gemini_chat.py
│   ├── chat_memory.py
│   └── voice_input.py
│
├── document_qa/          # Document processing logic
│   └── doc_chat.py
│
└── assets/               # UI design elements and images

---


## 🔑 Gemini API Setup

* **Step 1: Get API Key** Visit **[Google AI Studio](https://aistudio.google.com/)** to generate your unique API key.

* **Step 2: Configuration for Streamlit Cloud** * Navigate to your app dashboard: **App Settings** → **Secrets**.
  * Paste the following configuration:
    ```toml
    GEMINI_API_KEY = "your_api_key_here"
    ```

---

## ⚙️ Installation (Local Setup)

Follow these steps to run **ByteBuddy AI** on your local machine:

### **1️⃣ Clone the Repository**
```bash
git clone [https://github.com/Manu082/ByteBuddy-AI-Chatbot.git](https://github.com/Manu082/ByteBuddy-AI-Chatbot.git)
cd ByteBuddy-AI-Chatbot


