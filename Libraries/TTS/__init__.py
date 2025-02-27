"""
Text To Speech Module For Vikas AI.

Credits: Brian TTS Reader .
Link: https://github.com/5E7EN/TTS-Emulator .
"""
import requests
import os
import rich
import asyncio
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Set the relative path to where your script is located
relative_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


async def download_tts(text):
    """Asynchronous function to request TTS audio file."""
    voice = "Brian"  # Use Brian's voice from StreamElements
    api_url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={text}"

    # Make the asynchronous request to the StreamElements API
    response = await asyncio.to_thread(requests.get, api_url, params={})

    if response.status_code != 200:
        print("Error:", response.text)
        return None

    # Path to save the audio file
    audio_file_path = os.path.join(relative_path, "Data", "TTS", "TTS.mp3")

    # Write the audio response to the file asynchronously
    with open(audio_file_path, "wb") as f:
        f.write(response.content)

    return audio_file_path


async def play_audio(audio_file_path):
    """Asynchronous function to play the audio."""
    # Load the audio file
    pygame.mixer.music.load(audio_file_path)

    # Start playing the audio
    pygame.mixer.music.play()

    # Wait until the sound finishes playing
    while pygame.mixer.music.get_busy():
        # Sleep to avoid 100% CPU usage while waiting for sound to finish
        await asyncio.sleep(0.1)


async def speak_async(text, print_msg=True):
    """Main function to handle TTS and play speech asynchronously."""
    # Print the message if user permitted
    if print_msg:
        rich.print(f"Vikas AI: {text}", flush=True)

    # Download the TTS audio file asynchronously
    audio_file_path = await download_tts(text)

    if audio_file_path:
        # Play the downloaded audio in parallel with other tasks
        await play_audio(audio_file_path)


def speak(text, print_msg=True):
    """Entry point for asyncio execution."""
    asyncio.run(speak_async(text,print_msg))
if __name__ == "__main__":
    speak("""Allow me to introduce myself, I am Vikas AI, your personal assistant designed to help you with a variety of tasks and make your life easier.""")