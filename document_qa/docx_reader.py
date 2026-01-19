"""
ByteBuddy AI - DOCX Reader Module
--------------------------------
This module extracts and cleans text from Microsoft Word (.docx)
files for intelligent Document Q&A using Gemini AI.
"""

import docx


def read_docx(file):
    """
    Reads a DOCX file uploaded via Streamlit and extracts text safely.

    Args:
        file (UploadedFile): Streamlit uploaded DOCX file

    Returns:
        str: Extracted and cleaned text content
    """

    try:
        document = docx.Document(file)
        text = ""

        # Read all paragraphs
        for para in document.paragraphs:
            if para.text.strip():
                text += para.text + "\n"

        # Basic cleaning
        text = text.replace("\t", " ")
        text = text.replace("\r", " ")
        text = "\n".join(
            line.strip() for line in text.split("\n") if line.strip()
        )

        if not text:
            return "⚠️ No readable text found in this DOCX file."

        return text

    except Exception as e:
        return f"❌ Error reading DOCX file: {str(e)}"
