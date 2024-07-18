#çeviri uygulaması yapma
from gtts import gTTS
import os

chose= input("""
1. Türkçe
2.English
3.Espayol
4.Russia
5.Italion
6.French
7.Chinese
8.Korean
Yukarıdaki seçeneklereden birini seçiniz:
""")
lang=None
if chose =="1":
    lang= "tr"
elif chose =="2":
    lang= "en"
elif chose =="3":
    lang= "es"
elif chose =="4":
    lang= "ru"
elif chose =="5":
    lang= "it"
elif chose =="6":
    lang= "fr"
elif chose =="7":
    lang= "zh-CN"
elif chose == "8":
    lang = "ko"
else:
    print("Lütfen geçerli bir dil seçiniz.")

text=input("Please select a language:\n")
translate=gTTS(text=text,lang=lang) #metinden sese dönüştürme kodu
translate.save("texttospeech.mp3") #ses dosyasını kaydet

os.system("texttospeech.mp3")