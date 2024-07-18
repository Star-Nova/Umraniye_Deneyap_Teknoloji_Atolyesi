#Sesi metne çevirme
import sounddevice as sd
import speech_recognition as sr
import speech_recognition_python


def main():
    r=sr.Recognizer() #Ses tanıma işini yapan fonk
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) #arka plan seslerini temizliyor
        print("Konuşur musun?")
        audio=r.listen(source,timeout=10) #Mikrofonu dinler
        print("You said: \n"+ r.recognize_google(audio))#sesi metne çevirir


main()