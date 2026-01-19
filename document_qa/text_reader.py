"""
ByteBuddy AI - Text File Reader Module
-------------------------------------
This module handles reading and cleaning text files (.txt)
for Document Q&A using Gemini AI.
"""

def read_txt(file):
    """
    Reads a TXT file uploaded via Streamlit and returns cleaned text.

    Args:
        file (UploadedFile): Streamlit uploaded .txt file

    Returns:
        str: Extracted and cleaned text content
    """

    try:
        # Read bytes and decode safely
        raw_text = file.read()

        try:
            text = raw_text.decode("utf-8")
        except UnicodeDecodeError:
            # Fallback for non-utf8 encodings
            text = raw_text.decode("latin-1")

        # Basic text cleaning
        text = text.replace("\t", " ")
        text = text.replace("\r", " ")
        text = "\n".join(
            line.strip() for line in text.split("\n") if line.strip()
        )

        if not text:
            return "⚠️ The text file is empty or unreadable."

        return text

    except Exception as e:
        return f"❌ Error reading text file: {str(e)}"
