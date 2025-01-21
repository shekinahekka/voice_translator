import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

# Create recognizer instance
recognizer = sr.Recognizer()

# Capture voice input
with sr.Microphone() as source:
    print("Speak Now")
    voice = recognizer.listen(source)

# Recognize speech
try:
    text = recognizer.recognize_google(voice, language="en")  # Ensure language code is correct
    print(f"Recognized text: {text}")

    # Translate text
    translator = Translator()
    translation = await translator.translate(text, dest="fr")  # Translate to English for demonstration
    print(f"Translated text: {translation.text}")

    # Convert translation to speech
    converted_audio = gTTS(translation.text, lang="en")
    current_directory = os.getcwd()
    save_directory= os.path.join(current_directory, "hello.mp3")
    converted_audio.save(save_directory)
    playsound.playsound(save_directory)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print(f"Error with Google API: {e}")
