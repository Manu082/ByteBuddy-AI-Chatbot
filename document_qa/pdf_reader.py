"""
ByteBuddy AI - PDF Reader Module
--------------------------------
This module extracts and cleans text from PDF files
for intelligent Document Q&A using Gemini AI.
"""

import PyPDF2


def read_pdf(file):
    """
    Reads a PDF file uploaded via Streamlit and extracts text safely.

    Args:
        file (UploadedFile): Streamlit uploaded PDF file

    Returns:
        str: Extracted and cleaned text content
    """

    try:
        reader = PyPDF2.PdfReader(file)
        text = ""

        # Loop through all pages
        for page_number, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text()

            if page_text:
                text += f"\n--- Page {page_number} ---\n"
                text += page_text

        # Basic cleaning
        text = text.replace("\t", " ")
        text = text.replace("\r", " ")
        text = "\n".join(
            line.strip() for line in text.split("\n") if line.strip()
        )

        if not text:
            return "⚠️ No readable text found in this PDF."

        return text

    except Exception as e:
        return f"❌ Error reading PDF file: {str(e)}"
