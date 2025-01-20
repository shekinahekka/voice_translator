import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound

# Create recognizer instance
recognizer = sr.Recognizer()

# Capture voice input
with sr.Microphone() as source:
    print("Speak Now")
    voice = recognizer.listen(source)

# Recognize speech
try:
    text = recognizer.recognize_google_cloud(voice, language="fr-FR")  # Ensure language code is correct
    print(f"Recognized text: {text}")

    # Translate text
    translator = Translator()
    translation = translator.translate(text, dest="en")  # Translate to English for demonstration
    print(f"Translated text: {translation.text}")

    # Convert translation to speech
    converted_audio = gTTS(translation.text, lang="en")
    converted_audio.save("hello.mp3")
    playsound.playsound("hello.mp3")
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print(f"Error with Google API: {e}")