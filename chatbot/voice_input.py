"""
ByteBuddy AI - Voice Input Module
--------------------------------
Captures voice input from microphone
and converts it to text.
"""

import speech_recognition as sr


def listen_from_mic():
    """
    Listens to user's voice and converts it to text.

    Returns:
        str: Recognized text or error message
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio)
        return text

    except sr.WaitTimeoutError:
        return "⚠️ Listening timed out. Please try again."

    except sr.UnknownValueError:
        return "⚠️ Could not understand your voice."

    except sr.RequestError:
        return "❌ Speech recognition service unavailable."

    except Exception as e:
        return f"❌ Voice error: {str(e)}"
