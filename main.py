"""
RoboSpeaker 1.1
Created by Vaibhao Hatwar

A simple cross-platform Python text-to-speech program.
Supports macOS, Windows, and Linux.
"""

import os
import platform

# Try importing pyttsx3 for Windows TTS
try:
    import pyttsx3
except ImportError:
    pyttsx3 = None


def speak(text):
    """
    Speak the given text depending on the operating system.

    macOS: Uses the 'say' command
    Windows: Uses pyttsx3 library
    Linux: Uses 'espeak' command
    """
    system = platform.system()

    if system == "Darwin":  # macOS
        # Wrap text in quotes to handle spaces/special characters
        os.system(f'say "{text}"')
    elif system == "Windows":
        if pyttsx3 is None:
            print("Install pyttsx3 to enable speech: pip install pyttsx3")
        else:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
    elif system == "Linux":
        # Wrap text in quotes for spaces/special characters
        os.system(f"espeak '{text}'")
    else:
        print("Sorry, your OS is not supported for speech output.")


if __name__ == "__main__":
    # Welcome message
    print("Welcome to RoboSpeaker 1.1. Created by Vaibhao")
    print("Enter 'q' when you want to exit")  # Instruct user how to quit

    # Main loop for continuous user input
    while True:
        user_input = input("Enter what you want me to speak: ")
        if user_input.lower() == 'q':  # Exit if user types 'q' (case-insensitive)
            speak("Thank you for playing RoboSpeaker, bye bye, see you again!")
            break
        speak(user_input)