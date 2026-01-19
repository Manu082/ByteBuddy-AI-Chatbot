# 🤖 **ByteBuddy AI Chatbot**

**ByteBuddy AI** is a professional AI chatbot platform built using **Python**, **Streamlit**, and **Google Gemini API**. It integrates **AI chat**, **document analysis**, and **voice commands** into a single interface.

---

### 🚀 **Key Features**

* **💬 AI Chat:** **Natural language** interaction with **context-aware** chat memory.
* **📄 Document Q&A:** Support for **PDF**, **DOCX**, and **TXT** file analysis.
* **🎤 Voice Assistant:** Integrated **voice-to-text** for hands-free queries.
* **🌗 UI Customization:** Smooth toggle between **Light** and **Dark** modes.
* **🧠 Session Memory:** Retains **conversation history** throughout the session.

---
## 📁 Project Structure
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

### 🛠️ **Tech Stack**

* **Frontend:** **Streamlit**, **Custom HTML**, and **CSS Animations**.
* **Backend:** **Python** logic and **Document Parsing**.
* **AI Engine:** **Google Gemini API** (Flash & Pro models).
* **Embeddings:** **Gemini Embeddings** for document retrieval.

---

### 🔑 **Gemini API Setup**

* **Step 1:** Generate your key at **Google AI Studio**.
* **Step 2:** Add your key to **Streamlit Secrets**:
    ```toml
    GEMINI_API_KEY = "your_api_key_here"
    ```

---

### ⚙️ **Installation (Local Setup)**

* **Clone Repository:**
    ```bash
    git clone [https://github.com/Manu082/ByteBuddy-AI-Chatbot.git](https://github.com/Manu082/ByteBuddy-AI-Chatbot.git)
    cd ByteBuddy-AI-Chatbot
    ```
* **Environment Setup:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Use venv\Scripts\activate for Windows
    ```
* **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
* **Run Application:**
    ```bash
    streamlit run app.py
    ```

---

### 📌 **Technical Details**

* **Deployment:** Hosted on **Streamlit Cloud**.
* **Models:** Support for **Gemini-Flash-Latest** and **Gemini-Pro-Latest**.
* **Structure:** Organized modularly into **chatbot/** and **document_qa/** directories.

---

### 👨‍💻 **Author & Credits**

* **Author:** **Manas Didwania**
* **Acknowledgements:** **Google Gemini API**, **Streamlit**, and the **Open Source Community**.
