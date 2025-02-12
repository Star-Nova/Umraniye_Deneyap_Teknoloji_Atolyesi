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
from datetime import datetime  # Tarih ve saat için gereken modül

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
        os.system(
            f"osascript -e 'tell application \"System Events\" to set the value of the first slider of the first group of the first window of (first process whose frontmost is true) to {value}'")
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
        with open('hobby.txt', 'r') as file:
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
        with open('Desserts.txt', 'r') as file:
            desserts = file.readlines()
            if desserts:
                dessert = random.choice(desserts).strip()
                webbrowser.open(f"https://www.youtube.com/results?search_query={dessert}")
                return dessert
            else:
                return "Dessert list is empty."
    except FileNotFoundError:
        return "Desserts.txt file not found."


def suggest_meatdishes():
    try:
        with open('meatdishes.txt', 'r') as file:
            meatdishes = file.readlines()
            if meatdishes:
                meatdish = random.choice(meatdishes).strip()
                return meatdish
            else:
                return "Meat Dishes list is empty."
    except FileNotFoundError:
        return "meatdishes.txt file not found."


def suggest_vegetabledishes():
    try:
        with open('vegetabledishes.txt', 'r') as file:
            vegetabledishes = file.readlines()
            if vegetabledishes:
                vegetabledish = random.choice(vegetabledishes).strip()
                return vegetabledish
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
                return "Salad list is empty."
    except FileNotFoundError:
        return "salad.txt file not found."


def suggest_hamurisleri():
    try:
        with open('hamurisleri.txt', 'r') as file:
            hamurisleri = file.readlines()
            if hamurisleri:
                hamur = random.choice(hamurisleri).strip()
                return hamur
            else:
                return "Hamur işleri listesi boş."
    except FileNotFoundError:
        return "hamurisleri.txt dosyası bulunamadı."


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

#oyun tercihi yapar
    #savaş oyunu tercihi
def suggest_wargame():
    try:
        with open('wargame.txt', 'r') as file:
            wargame = file.readlines()
            if wargame:
                wargames = random.choice(wargame).strip()
                return wargames
            else:
                return "War Game list is empty."
    except FileNotFoundError:
        return "wargame.txt file not found."

    #hikaye oyunu
def suggest_storygame():
    try:
        with open('storygame.txt', 'r') as file:
            storygame = file.readlines()
            if storygame:
                storygames = random.choice(storygame).strip()
                return storygames
            else:
                return "Story Game list is empty."
    except FileNotFoundError:
        return "storygame.txt file not found."

    #yaratıcılık oyunu
def suggest_creativitygame():
    try:
        with open('creativitygame.txt', 'r') as file:
            creativitygame = file.readlines()
            if creativitygame:
                creativitygames = random.choice(creativitygame).strip()
                return creativitygames
            else:
                return "Creativity Game list is empty."
    except FileNotFoundError:
        return "creativitygame.txt file not found."

#film tercihi yapar

    #aksiyon film önerir
def suggest_actionfilm():
    try:
        with open('actionfilm.txt', 'r') as file:
            actionfilm = file.readlines()
            if actionfilm:
                actionfilms = random.choice(actionfilm).strip()
                return actionfilms
            else:
                return "Action Film list is empty."
    except FileNotFoundError:
        return "actionfilm.txt file not found."

    #komedi film önerir
def suggest_comedyfilm():
    try:
        with open('comedyfilm.txt', 'r') as file:
            comedyfilm = file.readlines()
            if comedyfilm:
                comedyfilms = random.choice(comedyfilm).strip()
                return comedyfilms
            else:
                return "Comedy film list is empty."
    except FileNotFoundError:
        return "comedyfilm.txt file not found."

    # Drama tarzı film önerir
def suggest_dramafilm():
    try:
        with open('dramafilm.txt', 'r') as file:
            dramafilm = file.readlines()
            if dramafilm:
                dramafilms = random.choice(dramafilm).strip()
                return dramafilms
            else:
                return "Drama Film list is empty."
    except FileNotFoundError:
        return "dramafilm.txt file not found."

    #korku filmi önerir
def suggest_horrorfilm():
    try:
        with open('horrorfilm.txt', 'r') as file:
            horrorfilm = file.readlines()
            if horrorfilm:
                horrorfilms = random.choice(horrorfilm).strip()
                return horrorfilms
            else:
                return "Horror Film list is empty."
    except FileNotFoundError:
        return "horrorfilm.txt file not found."

    #bilim kurgu filmi önerir
def suggest_science_fiction_film():
    try:
        with open('sciencefictionfilm.txt', 'r') as file:
            science_fiction_film = file.readlines()
            if science_fiction_film:
                science_fiction_films = random.choice(science_fiction_film).strip()
                return science_fiction_films
            else:
                return "Science fiction film list is empty."
    except FileNotFoundError:
        return "sciencefictionfilm.txt file not found."

    #romantik tarzı filmler önerir
def suggest_romantic_film():
    try:
        with open('romanticfilm.txt', 'r') as file:
            romantic_film = file.readlines()
            if romantic_film:
                romantic_films = random.choice(romantic_film).strip()
                return romantic_films
            else:
                return "Romantic Film list is empty."
    except FileNotFoundError:
        return "romanticfilm.txt file not found."

   #Belgesel tarzı
def suggest_documentary_film():
    try:
        with open('documentaryfilm.txt', 'r') as file:
            documentary_film = file.readlines()
            if documentary_film:
                documentary_films = random.choice(documentary_film).strip()
                return documentary_films
            else:
                return "Documentary Film list is empty."
    except FileNotFoundError:
        return "documentaryfilm.txt file not found."

    #animasyon tarzı film
def suggest_animation_film():
    try:
        with open('animationfilm.txt', 'r') as file:
            animation_film = file.readlines()
            if animation_film:
                animation_films = random.choice(animation_film).strip()
                return animation_films
            else:
                return "Animation Film list is empty."
    except FileNotFoundError:
        return "animationfilm.txt file not found."

    #tarihi film
def suggest_historic_film():
    try:
        with open('historicfilm.txt', 'r') as file:
            historic_film = file.readlines()
            if historic_film:
                historic_films = random.choice(historic_film).strip()
                return historic_films
            else:
                return "Historical Film list is empty."
    except FileNotFoundError:
        return "historicfilm.txt file not found."


#şarkı tercihi yapar
#def suggest_song():
    #try:
        #with open('icecream.txt', 'r') as file:
            #song = file.readlines()
            #if song:
                #songs = random.choice(song).strip()
                #return songs
            #else:
                #return "Song list is empty."
        #except FileNotFoundError:
        #return "icecream.txt file not found."

#kodlarını çözer
def solve_code_problem():
    speak("Please describe the coding problem you are facing.")
    problem = listen()
    speak("I will try to help with that coding problem.")
    # Implement the logic to solve the problem or provide suggestions
    # This could involve searching online or providing code snippets

#tarihi söyler
def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

#sohbet kodları
def chat_english():
    speak("Sure, let's chat. How are you today?")
    user_response = listen()

    if user_response in ["good", "fine", "great", "okay"]:
        speak("I'm glad to hear that! What have you been up to lately?")
    elif user_response in ["not good", "bad", "not great"]:
        speak("I'm sorry to hear that. Is there anything specific that's bothering you?")
    else:
        speak("I see. What would you like to talk about today?")

    user_response = listen()
    if "weather" in user_response:
        speak("The weather is quite interesting today. Do you like the current weather?")
    elif "hobbies" in user_response:
        speak("Hobbies are a great way to relax. What hobbies do you enjoy?")
    elif "news" in user_response:
        speak("There are many interesting news stories today. Are you following any particular news?")
    elif "movies" in user_response:
        speak("Movies can be a lot of fun. Do you have a favorite movie or genre?")
    elif "music" in user_response:
        speak("Music is a great way to lift your mood. What kind of music do you like?")
    elif "food" in user_response:
        speak("Food can be so enjoyable. Do you have a favorite dish or type of cuisine?")
    elif "travel" in user_response:
        speak("Traveling opens up new experiences. Where would you like to travel next?")
    elif "books" in user_response:
        speak("Books can be quite engaging. Are you reading any interesting books right now?")
    else:
        speak("That sounds interesting! Is there anything else you'd like to discuss?")


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
#çeşitli tarayıcıları açar
        elif 'open bing' in query:
            webbrowser.open("https://www.bing.com")
        elif 'open opera' in query:
            webbrowser.open("https://www.opera.com")
        elif 'open chrome' in query:
            webbrowser.open("https://www.google.com/chrome/")
        elif 'open safari' in query:
            webbrowser.open("https://www.apple.com/safari/")
        elif 'open firefox' in query:
            webbrowser.open("https://www.mozilla.org/firefox/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
#sosyal medya sitelerini açar
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/")
        elif 'open x' in query:
            webbrowser.open("https://x.com/")
        elif 'open twitter' in query:
            webbrowser.open("https://x.com/")
        elif 'open WhatsApp' in query:
            webbrowser.open("https://www.whatsapp.com")
        elif 'open WhatsApp web' in query:
            webbrowser.open("https://web.whatsapp.com")
        elif 'open WhatsApp web ' in query:
            webbrowser.open("https://web.whatsapp.com")
        elif 'open reddit' in query:
            webbrowser.open("https://www.reddit.com")
        elif 'open pinterest' in query:
            webbrowser.open("https://www.pinterest.com")
        elif 'open snapchat' in query:
            webbrowser.open("https://www.snapchat.com")
        elif 'open tik tok' in query:
            webbrowser.open("https://www.tiktok.com")
        elif 'open netflix' in query:
            webbrowser.open("https://www.netflix.com/")
        elif 'open discord' in query:
            webbrowser.open("https://discord.com/")
        elif 'open GitHub' in query:
            webbrowser.open("https://github.com/")
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


#sana şarkı önerir
        #elif 'suggest me a song' in query:
           #icecream = suggest_icecream()
            #speak(f"How about: {icecream}")


if __name__ == "__main__":
    run_assistant()
    
#CREDIT KOD_YAZARI
