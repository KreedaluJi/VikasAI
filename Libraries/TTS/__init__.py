"""
This is the tts module for Vikas AI.
"""

# Module For TTS
import pyttsx3

# Initializing Speech engine and setting the required properties
engine = pyttsx3.init("sapi5", debug=False)
voices = engine.getProperty("voices")
engine.setProperty(
    "voice",
    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\IVONA 2 Voice Brian22",
)


# The Speak Function
def speak(text, print_msg=True) -> None:
    """
    This is the speech function for Vikas.
    :param text:
    :param print_msg:
    :return: None:
    """
    if print_msg:
        print(f"Vikas: {text}")
    engine.say(text)
    engine.runAndWait()


# Testing The Function
if __name__ == "__main__":
    speak(
        "Allow Me To introduce myself, i am vikas Ai, a personal assistant designed to assist you with a variety of tasks."
    )