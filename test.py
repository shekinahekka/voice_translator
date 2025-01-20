import googletrans
import speech_recognition
import gtts
import playsound
recognizer= speech_recognition.Recognizer()
attributes = set(dir(recognizer))
"recognize_google" in attributes

with speech_recognition.Microphone() as source:
    print("speak now ")
    voice= recognizer.listen(source)
    text= recognizer.recognize_google(voice, language="fr")
    print(text)
translator= googletrans.Translator()
translation= translator.translate(text, dest="fr")
print(translation.text)
converted = gtts.gTTS(translation.text, lang="fr")
converted.save("hello.mp3")
playsound.playsound("hello.mp3")

#print(googletrans.LANGUAGES)