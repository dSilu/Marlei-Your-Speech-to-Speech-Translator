import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr. Recognizer()

my_lang = 'en'
other_lang = 'hi'

# source: Assigning microphone as the voice input source for the machine
with sr.Microphone() as source:
    print('Speak to me')
    # listening the speech
    voice = recognizer.listen(source)
    # Speech to text conversion
    text = recognizer.recognize_google(voice, language=my_lang)  # the other language goes here


def translate(text):
    translator = googletrans.Translator()

    # translating the speech
    translated = translator.translate(text, dest=other_lang)
    print(translated.text)

    # converting the translated text to speech
    converted_speech = gtts.gTTS(translated.text)
    converted_speech.save('my_translator.mp3')

    # voice output
    play =playsound.playsound('my_translator.mp3')
    return playsound


print(text)
print(translate(text))