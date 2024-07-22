#çeviri çalışmıyor
#brightness çalışmıyor
#volume çalışmıyor
#dessert çalışmıyor
import os
import platform
import pyautogui
import pyttsx3
import speech_recognition as sr
import pyjokes
import requests
import smtplib, ssl
import time
import wikipedia
import webbrowser
from PIL import Image
from googletrans import Translator
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
import random

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

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error during calculation: {e}")
        return None

def send_email(sender_email, sender_password, receiver_email, subject, body):
    smtp_server = "smtp.gmail.com"
    port = 587

    message = f"Subject: {subject}\n\n{body}"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

def get_location_from_ip(ip_address):
    ipstack_api_key = "YOUR_IPSTACK_API_KEY"
    base_url = f"http://api.ipstack.com/{ip_address}?access_key={ipstack_api_key}"

    response = requests.get(base_url)
    data = response.json()

    if 'city' in data and 'region_name' in data:
        city = data['city']
        region = data['region_name']
        return city, region
    else:
        return None, None

def translate_text(text, dest_language):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return "Sorry, I couldn't perform the translation."

def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        description = weather["description"]
        weather_report = f"The temperature in {city} is {temp} degrees Celsius with {description}."
        return weather_report
    else:
        return "City not found."

def wait(duration, unit):
    if unit == "minutes":
        time.sleep(duration * 60)
    elif unit == "seconds":
        time.sleep(duration)
    speak(f"Waited for {duration} {unit}")

def set_brightness(level):
    system = platform.system()
    if system == 'Windows':
        if level == 'high':
            value = 100
        elif level == 'medium':
            value = 50
        elif level == 'low':
            value = 0
        else:
            return
        # Simulated brightness control
        print(f"Set brightness to {value}%")
    elif system == 'Darwin':
        if level == 'high':
            value = 100
        elif level == 'medium':
            value = 50
        elif level == 'low':
            value = 0
        else:
            return
        os.system(f"osascript -e 'tell application \"System Events\" to set the value of the first slider of the first group of the first window of (first process whose frontmost is true) to {value}'")
    elif system == 'Linux':
        if level == 'high':
            value = 1.0
        elif level == 'medium':
            value = 0.5
        elif level == 'low':
            value = 0.1
        else:
            return
        os.system(f"xrandr --output eDP-1 --brightness {value}")

def set_volume(level):
    system = platform.system()
    if system == 'Windows':
        if level == 'high':
            value = 1.0
        elif level == 'medium':
            value = 0.5
        elif level == 'low':
            value = 0.0
        else:
            return
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(ISimpleAudioVolume._iid_, CLSCTX_ALL, None)
        volume = interface.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(value, None)
    elif system == 'Darwin':
        if level == 'high':
            value = 100
        elif level == 'medium':
            value = 50
        elif level == 'low':
            value = 0
        else:
            return
        os.system(f"osascript -e 'set volume output volume {value}'")
    elif system == 'Linux':
        if level == 'high':
            value = 100
        elif level == 'medium':
            value = 50
        elif level == 'low':
            value = 0
        else:
            return
        os.system(f"pactl set-sink-volume 0 {value}%")

def take_screenshot(filename):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    img = Image.open(filename)
    img.show()

def suggest_hobby():
    try:
        with open(' hobby.txt', 'r') as file:
            hobbies = file.readlines()
            if hobbies:
                hobby = random.choice(hobbies).strip()
                return hobby
            else:
                return "Hobby list is empty."
    except FileNotFoundError:
        return "hobby.txt file not found."

def suggest_dessert():
    try:
        with open('tatli.txt', 'r') as file:
            desserts = file.readlines()
            if desserts:
                dessert = random.choice(desserts).strip()
                return dessert
            else:
                return "Dessert list is empty."
    except FileNotFoundError:
        return "tatli.txt file not found."

def suggest_meatdishes():
    try:
        with open('meatdishes.txt', 'r') as file:
            meatdishess = file.readlines()
            if meatdishess:
                meatdishes = random.choice(meatdishess).strip()
                return meatdishes
            else:
                return "Meat Dishes list is empty."
    except FileNotFoundError:
        return "meatdishes.txt file not found."

def suggest_vegetabledishes():
    try:
        with open('vegetabledishes.txt', 'r') as file:
            vegetabledishess = file.readlines()
            if vegetabledishess:
                vegetabledishes = random.choice(vegetabledishess).strip()
                return vegetabledishes
            else:
                return "Vegetable Dishes list is empty."
    except FileNotFoundError:
        return "vegetabledishes.txt file not found."

def suggest_soup():
    try:
        with open('soup.txt', 'r') as file:
            soups = file.readlines()
            if soups:
                soup = random.choice(soups).strip()
                return soup
            else:
                return "Soup list is empty."
    except FileNotFoundError:
        return "soup.txt file not found."

def suggest_bread():
    try:
        with open('bread.txt', 'r') as file:
            breads = file.readlines()
            if breads:
                bread = random.choice(breads).strip()
                return bread
            else:
                return "Bread list is empty."
    except FileNotFoundError:
        return "bread.txt file not found."

def suggest_salad():
    try:
        with open('salad.txt', 'r') as file:
            salads = file.readlines()
            if salads:
                salad = random.choice(salads).strip()
                return salad
            else:
                return "Salads list is empty."
    except FileNotFoundError:
        return "salad.txt file not found."

def suggest_hamurisleri():
    try:
        with open('hamurisleri.txt', 'r') as file:
            hamurisleris = file.readlines()
            if hamurisleris:
                hamurisleri = random.choice(hamurisleris).strip()
                return hamurisleri
            else:
                return "Pastries list is empty."
    except FileNotFoundError:
        return "hamurisleri.txt file not found."

def suggest_icecream():
    try:
        with open('icecream.txt', 'r') as file:
            icecreams = file.readlines()
            if icecreams:
                icecream = random.choice(icecreams).strip()
                return icecream
            else:
                return "Ice cream list is empty."
    except FileNotFoundError:
        return "icecream.txt file not found."

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
            speak("Yes I love you because you create me")
        elif "what is your favorite country" in query:
            speak("My favorite country is Japan and China. Because people are very hardworking.")
        elif "who made you" in query:
            speak("Ege Tanriverdi made me. Notorious Code Writer.")
        elif "artificial intelligence examples" in query:
            speak("I can give Atlantic, ChatGPT, Perplexity, Gemini and Copilot as examples.")
        elif "what is your favorite color" in query:
            speak("My favorite color is blue.")
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
        elif 'suggest me a hobby' in query:
            hobby = suggest_hobby()
            speak(f"How about: {hobby}")
        elif 'suggest me a desert' in query:
            tatli = suggest_dessert()
            speak(f"How about: {tatli}")
        elif 'suggest me a meat dishes' in query:
            meat_dishes = suggest_meatdishes()
            speak(f"How about: {meat_dishes}")
        elif 'suggest me a vegetable dishes' in query:
            vegetable_dishes = suggest_vegetabledishes()
            speak(f"How about: {vegetable_dishes}")
        elif 'suggest me a soup' in query:
            soup = suggest_soup()
            speak(f"How about: {soup}")
        elif 'suggest me a salad' in query:
            salad = suggest_salad()
            speak(f"How about: {salad}")
        elif 'suggest me a bread' in query:
            bread = suggest_bread()
            speak(f"How about: {bread}")
        elif 'suggest me a pastries' in query:
            hamurisleri = suggest_hamurisleri()
            speak(f"How about: {hamurisleri}")
        elif 'suggest me an ice cream' in query:
            icecream = suggest_icecream()
            speak(f"How about: {icecream}")

if __name__ == "__main__":
    run_assistant()

#Credit Kod_Yazarı
