import googletrans
import speech_recognition as sr
import gtts
import playsound

def main(user):
    global my_lang
    global other_lang 

    print("Hi! Marlei here")
    greetings = gtts.gTTS("Hello there I am your Translator Marlei, Choose your languages", lang='en', slow=False)
    greetings.save('Marlei_greetings.mp3')
    playsound.playsound('Marlei_greetings.mp3')
    my_lang = input("Your language: ")
    other_lang = input("Your audince's language: ")
    translate(user)
    print('*_*')

def translate(user):
    global my_lang
    global other_lang

    translater = googletrans.Translator()
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak To Me: ")
        voice = recognizer.listen(source)
        user = recognizer.recognize_google(voice, language=my_lang)
        print(user)

    translated = translater.translate(user, dest=other_lang)
    print(translated.text)

    convert_t2s = gtts.gTTS(translated.text, lang=other_lang)
    convert_t2s.save('Marlei.mp3')

    playsound.playsound('Marlei.mp3')
    


if __name__ == '__main__':
    main(user=sr.Microphone)