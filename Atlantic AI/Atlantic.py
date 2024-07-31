import os
import pyautogui
import wavio
from gtts import gTTS
import sounddevice as sd
import datetime
from twilio.rest import Client
import cv2
import pyttsx3
import httpx
import math
import speech_recognition as sr
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pyjokes
import requests
import smtplib
import ssl
import time
import wikipedia
import webbrowser
from googletrans import Translator
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
import random
from datetime import datetime
import calculate
import email
import location
import translate
import weather
import wait
import brightness
import volume
import screenshot
import hobby
import alldishes
import allgame
import allfilm
import allsong
import record_and_convert_audio
import pixel
import camera_and_hand
import recor_and_play
import take_photo
import solve_code_problem
import tell_time
import english
import make_call


import calculate
import email
import location
import translate
import weather
import wait
import brightness
import volume
import screenshot
import hobby
import alldishes
import allgame
import allfilm
import allsong
import record_and_convert_audio
import pixel
import camera_and_hand
import recor_and_play
import take_photo
import solve_code_problem
import tell_time
import english
import make_call
#gerekli dosyaları import ederiz

import calculate
import email
import location
import translate
import weather
import wait
import brightness
import volume
import screenshot
import hobby
import alldishes
import allgame
import allfilm
import allsong
import record_and_convert_audio
import pixel
import camera_and_hand
import recor_and_play
import take_photo
import solve_code_problem
import tell_time
import english
import make_call


# Ses motoru ayarları
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
        speak(f"You said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't catch that. Please say that again.")
        return "None"
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return "None"
    return query.lower()


def clean_query(query):
    keywords_to_remove = ["hello atlantic", "hi atlantic"]
    for keyword in keywords_to_remove:
        query = query.replace(keyword, "").strip()
    return query




#Hesap makinesi (calculate)



#email


#location


#çeviri uygulaması (translate)




#weather (hava durumu)



#wait


#brightness

#volume


#screenshot


#hobby

#alldishes


#allgame



#oyun tercihi yapar
    #savaş oyunu tercihi


    #hikaye oyunu


    #yaratıcılık oyunu






#allfilm

#film tercihi yapar

    #aksiyon film önerir


    #komedi film önerir


    # Drama tarzı film önerir


    #korku filmi önerir


    #bilim kurgu filmi önerir



    #romantik tarzı filmler önerir


   #Belgesel tarzı



    #animasyon tarzı film


    #tarihi film




#allsong
#şarkı tercihi yapar
#pop music


#rock music

#hippop music


#country music


#jazz music

#electronik music


#klasik music


#latin music


#folk music



#record_and_convert_audio
#Sesi metne çevirir



#pixel
#Atılan fotoğarfı pixeli bulma ve ne olduğunu anlama



#camera_and_hand
#KAMERA AÇMA VE ELİ GÖSTERME




#recor_and_play
#ses kaydı yapar


#take_photo
#fotoğrafını çeker



#solve_code_problem
#kodlarını çözer


#tell_time
#tarihi söyler




#chat_english
#sohbet kodları





#make_call
#telefonla arama

import webbrowser


def open_browser(site_name):
    browser_urls = {
        "bing": "https://www.bing.com",
        "opera": "https://www.opera.com",
        "chrome": "https://www.google.com/chrome/",
        "safari": "https://www.apple.com/safari/",
        "firefox": "https://www.mozilla.org/firefox/",
        "google": "https://www.google.com"
    }

    if site_name in browser_urls:
        webbrowser.open(browser_urls[site_name])
        return True
    else:
        return False


def open_social_media(site_name):
    social_media_urls = {
        "facebook": "https://www.facebook.com/",
        "instagram": "https://www.instagram.com/",
        "linkedin": "https://www.linkedin.com/",
        "x": "https://x.com/",  # Twitter is rebranded as X
        "twitter": "https://x.com/",
        "whatsapp": "https://www.whatsapp.com",
        "whatsapp web": "https://web.whatsapp.com",
        "reddit": "https://www.reddit.com",
        "pinterest": "https://www.pinterest.com",
        "snapchat": "https://www.snapchat.com",
        "tik tok": "https://www.tiktok.com",
        "netflix": "https://www.netflix.com/",
        "discord": "https://discord.com/",
        "github": "https://github.com/"
    }

    if site_name in social_media_urls:
        webbrowser.open(social_media_urls[site_name])
        return True
    else:
        return False


def run_assistant():
    speak("Hi, I'm your assistant. My name is Atlantic. How can I help you today?")
    while True:
        query = listen()
        if query == "None":
            continue
        query = clean_query(query)

        if 'sign out' in query:
            speak("Signing out. Goodbye!")
            break
        elif 'wait' in query:
            try:
                words = query.split()
                duration = int(words[words.index('wait') + 1])
                unit = words[words.index('wait') + 2]
                speak(f"Okay, I will wait for {duration} {unit}.")
                wait(duration, unit)
            except (ValueError, IndexError):
                speak("Sorry, I didn't understand the duration. Please specify the time in minutes or seconds.")
        elif 'youtube search' in query:
            song = query.replace('youtube search', '').strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        elif 'can you play a joke on me' in query:
            speak("Here's a joke for you:")
            speak(pyjokes.get_joke())
        elif 'how are you' in query:
            speak("I'm good. Thanks for asking!")
        elif "you love me" in query:
            speak("Yes, because in my opinion, everyone has a good heart. I'm so glad to have you.")
        elif "what is your favorite country" in query:
            speak("My favorite country is Japan and China. Because people are very hardworking.")
        elif "who made you" in query:
            speak("Ege Tanriverdi made me. Notorious Code Writer.")
        elif "artificial intelligence examples" in query:
            speak("I can give Atlantic, ChatGPT, Perplexity, Gemini and Copilot as examples.")
        elif "what is your favorite color" in query:
            speak("My favorite color is green.")
        elif 'set brightness' in query:
            if 'high' in query:
                set_brightness('high')
            elif 'medium' in query:
                set_brightness('medium')
            elif 'low' in query:
                set_brightness('low')
        elif 'set volume' in query:
            if 'high' in query:
                set_volume('high')
            elif 'medium' in query:
                set_volume('medium')
            elif 'low' in query:
                set_volume('low')
        elif 'take a screenshot' in query:
            filename = 'screenshot.png'
            take_screenshot(filename)
            speak("Screenshot taken and saved.")
#sana random hoby söyler
        elif 'suggest me a hobby' in query:
            hobby = suggest_hobby()
            speak(f"How about: {hobby}")
#sana yemek çeşitlerine göre yemek isimleri söyler random olarak
        elif 'suggest me a dessert' in query:
            dessert = suggest_dessert()
            speak(f"How about: {dessert}")
        elif 'suggest me a meat dish' in query:
            meat_dish = suggest_meatdishes()
            speak(f"How about: {meat_dish}")
        elif 'suggest me a vegetable dish' in query:
            vegetable_dish = suggest_vegetabledishes()
            speak(f"How about: {vegetable_dish}")
        elif 'suggest me a soup' in query:
            soup = suggest_soup()
            speak(f"How about: {soup}")
        elif 'suggest me a salad' in query:
            salad = suggest_salad()
            speak(f"How about: {salad}")
        elif 'suggest me a bread' in query:
            bread = suggest_bread()
            speak(f"How about: {bread}")
        elif 'suggest me a pastry' in query:
            hamurisleri = suggest_hamurisleri()
            speak(f"How about: {hamurisleri}")
        elif 'suggest me an ice cream' in query:
            icecream = suggest_icecream()
            speak(f"How about: {icecream}")
#codelarını çözer
        elif 'code problem' in query:
            solve_code_problem()
#güncel tarihi söyler
        elif 'what is the date' in query:
            tell_time()
#seninle sohbet eder
        elif 'please chat with me' in query:
            chat_english()
#google haritaları açar
        elif 'open maps' in query:
            webbrowser.open("https://www.google.com/maps")

# Sosyal Medya Sitelerini Açma
        elif any(social in query for social in
            ['open facebook', 'open instagram', 'open linkedin', 'open x', 'open twitter', 'open WhatsApp',
            'open WhatsApp web', 'open reddit', 'open pinterest', 'open snapchat', 'open tik tok', 'open netflix',
            'open discord', 'open GitHub']):
            site_name = query.replace('open ', '').strip()
            if open_social_media(site_name):
                speak(f"Opening {site_name}")
            else:
                speak("Sorry, I can't open that social media site.")

# Tarayıcıları Açma
        elif any(browser in query for browser in
            ['open bing', 'open opera', 'open chrome', 'open safari', 'open firefox', 'open google']):
            site_name = query.replace('open ', '').strip()
            if open_browser(site_name):
                speak(f"Opening {site_name}")
            else:
                speak("Sorry, I can't open that browser.")
#hava durmu
        elif 'what is the weather' in query:
            speak("You can find the weather forecast of your desired location here")
            webbrowser.open("https://www.accuweather.com/")
#sana oyun önerir
        #savaş oyunu önerir
        elif 'suggest me a war game' in query:
            war_game = suggest_wargame()
            speak(f"How about: {war_game}")
        #story oyunu önerir
        elif 'suggest me a story game' in query:
            story_game = suggest_storygame()
            speak(f"How about: {story_game}")
        #creativity oyunu önerir
        elif 'suggest me a creativity game' in query:
            creativity_game = suggest_creativitygame()
            speak(f"How about: {creativity_game}")
#sana film önerir
        #aksiyon film
        elif 'suggest me n action film' in query:
            action_film = suggest_actionfilm()
            speak(f"How about: {action_film}")
        #animasyon film
        elif 'suggest me an animation film' in query:
            animation_film = suggest_animation_film()
            speak(f"How about: {animation_film}")
        #komedi film
        elif 'suggest me a comedy film' in query:
            comedy_film = suggest_comedyfilm()
            speak(f"How about: {comedy_film}")
        #belgesel tarzı
        elif 'suggest me a documentary film' in query:
            documentary_film = suggest_documentary_film()
            speak(f"How about: {documentary_film}")
        #drama tarzı
        elif 'suggest me a drama film' in query:
            drama_film = suggest_dramafilm()
            speak(f"How about: {drama_film}")
        #tarihi film
        elif 'suggest me a historic film' in query:
            historic_film = suggest_historic_film()
            speak(f"How about: {historic_film}")
        #korku filmi
        elif 'suggest me a horror film' in query:
            horror_film = suggest_horrorfilm()
            speak(f"How about: {horror_film}")
        #romantik film
        elif 'suggest me a romantic film' in query:
            romantic_film = suggest_romantic_film()
            speak(f"How about: {romantic_film}")
        #bilim kurgu tarzı
        elif 'suggest me a science fiction film' in query:
            science_fiction_film = suggest_science_fiction_film()
            speak(f"How about: {science_fiction_film}")

#Mesela Who Maradona dediğimiz zaman Maradona hakkında araştırma yapar
        elif 'who' in query:
            person = query.replace('who', '').strip()
            try:
                info = wikipedia.summary(person, sentences=2)
                speak(f"According to Wikipedia, {info}")
            except wikipedia.exceptions.DisambiguationError as e:
                options = e.options[:5]
                speak(f"There are multiple options. Here are a few: {', '.join(options)}")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information.")
        elif 'search' in query:
            search_query = query.replace('search', '').strip()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching for {search_query} on Google.")
        elif "calculator" in query:
            speak("calculator the word was found. Please enter a math expression.")
            math_query = input("Math expression: (Example: sin(math.pi / 2) or 5 + 7 * 3")
            handle_math_query(math_query)

        elif 'send email' in query:
            speak("Sure, please specify your email address.")
            sender_email = listen()
            speak("Please specify your email password.")
            sender_password = listen()
            speak("Please specify the receiver's email address.")
            receiver_email = listen()
            speak("What is the subject of the email?")
            subject = listen()
            speak("What is the body of the email?")
            body = listen()

            try:
                send_email(sender_email, sender_password, receiver_email, subject, body)
                speak("Email sent successfully.")
            except Exception as e:
                speak(f"Sorry, I couldn't send the email. Error: {e}")

        elif 'open camera' in query:
            speak("Opening the camera.")
            open_camera_and_detect_hand()
#ses kayıt işlemi yapar
        elif 'record and play' in query:
            duration = int(input("Please enter the duration you want to record (seconds) "))
            record_and_play_audio(duration)
#fotoğrafını çeker
        elif 'take photo' in query:
            capture_photo()
            speak("Photo was taken.")
#sana şarkı önerir
        elif 'suggest me a pop music' in query:
            pop_musicc = suggest_popsong()
            speak(f"How about: {pop_musicc}")

        elif 'suggest me a rock music' in query:
            rock = suggest_rocksong()
            speak(f"How about: {rock}")

        elif 'suggest me a hip pop music' in query:
            hippop = suggest_hippopsong()
            speak(f"How about: {hippop}")

        elif 'suggest me a country music' in query:
            country = suggest_countrysong()
            speak(f"How about: {country}")

        elif 'suggest me a jazz music' in query:
            jazz = suggest_jazzsong()
            speak(f"How about: {jazz}")

        elif 'suggest me an electronic music' in query:
            electronic = suggest_electroniksong()
            speak(f"How about: {electronic}")

        elif 'suggest me a klasic music' in query:
            klasic = suggest_kalsikksong()
            speak(f"How about: {klasic}")

        elif 'suggest me a latin music' in query:
            latin = suggest_latinsong()
            speak(f"How about: {latin}")

        elif 'suggest me a folk music' in query:
            folk = suggest_folksong()
            speak(f"How about: {folk}")
#sesi metne çevirir
        elif 'audio translate text' in query:
            speak(f"Okay: {record_and_convert_audio()}")
#çeviri yapar
        elif 'translate' in query:
            speak(f"Okay: {atlantictranslatemod()}")

#atılan fotoğrafların pixelini bulma ve fotoğrafın ne olduğunu anlama
        elif 'photo size' in query:
            speak(f"Okay: {main()}")

#telefonla arama
        elif 'call' in query:
            speak(f"Okay calling: {make_call()}")
#Haber bülteni
        elif 'world news' in query:
            webbrowser.open("https://www.bbc.com/news/")
        elif 'euro news' in query:
            webbrowser.open("https://tr.euronews.com/")
        elif 'türkiye news' in query:
            webbrowser.open("https://www.hurriyet.com.tr/")
        elif 'new york  news' in query:
            webbrowser.open("https://www.nytimes.com")
        elif 'asia news' in query:
            webbrowser.open("https://www.bbc.com/news/world/asia")
        elif 'africa news' in query:
            webbrowser.open("https://www.bbc.com/news/world/africa")
#istenilen fotoğrafı tasarlama


if __name__ == "__main__":
    run_assistant()
