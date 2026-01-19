"""
ByteBuddy AI - Document Q&A Module
---------------------------------
This module connects document readers (PDF, DOCX, TXT)
with Gemini AI to answer questions strictly based on
uploaded document content.
"""

from chatbot.gemini_chat import ask_gemini
from document_qa.pdf_reader import read_pdf
from document_qa.docx_reader import read_docx
from document_qa.text_reader import read_txt


def document_question_answer(uploaded_file, user_question):
    """
    Answers a user's question based on the uploaded document.

    Args:
        uploaded_file (UploadedFile): File uploaded via Streamlit
        user_question (str): Question asked by the user

    Returns:
        str: AI-generated answer based strictly on document content
    """

    if uploaded_file is None:
        return "⚠️ No document uploaded."

    if not user_question or user_question.strip() == "":
        return "⚠️ Please ask a valid question."

    try:
        file_name = uploaded_file.name.lower()

        # ------------------ READ DOCUMENT ------------------ #
        if file_name.endswith(".pdf"):
            document_text = read_pdf(uploaded_file)

        elif file_name.endswith(".docx"):
            document_text = read_docx(uploaded_file)

        elif file_name.endswith(".txt"):
            document_text = read_txt(uploaded_file)

        else:
            return "❌ Unsupported file format. Please upload PDF, DOCX, or TXT."

        # Safety check
        if not document_text or document_text.startswith("⚠️") or document_text.startswith("❌"):
            return document_text

        # ------------------ GEMINI PROMPT ------------------ #
        prompt = f"""
You are ByteBuddy AI, an intelligent document analysis assistant.

IMPORTANT RULES:
- Answer ONLY from the provided document.
- If the answer is not present, say: "The document does not contain this information."
- Do NOT use external knowledge.
- Be clear, concise, and professional.

DOCUMENT CONTENT:
\"\"\"
{document_text}
\"\"\"

USER QUESTION:
{user_question}
"""

        # ------------------ GET AI RESPONSE ------------------ #
        answer = ask_gemini(prompt)

        return answer.strip()

    except Exception as e:
        return f"❌ Error processing document: {str(e)}"
