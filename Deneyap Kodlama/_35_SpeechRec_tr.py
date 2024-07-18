#sesi metne çevirme
import speech_recognition as sr


def tr():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        print("Konuşur musun lütfen?")
        voice = r.listen(mic)
        try:
            print("Bunları söylediniz: \n" + r.recognize_google(voice, language="tr-TR"))
        except sr.UnknownValueError:
            print("Ne dediğinizi anlayamadım.")
        except sr.RequestError:
            print("Google API'sine ulaşılamadı.")


tr()
