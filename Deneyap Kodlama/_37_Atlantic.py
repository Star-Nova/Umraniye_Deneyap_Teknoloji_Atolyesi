#çeviri çalışmıyor
#brightness çalışmıyor
#volume çalışmıyor
#What is your favorite country? ekelenecek (ekleyeceğim)
#Who made you? ekelenecek (ekleyeceğim)
#Artificial intelligence examples ekelenecek (ekleyeceğim)
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
    except Exception as e:
        print("Sorry, I couldn't catch that. Please say that again.")
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
        import win32api
        import win32con
        if level == 'high':
            value = 100
        elif level == 'medium':
            value = 50
        elif level == 'low':
            value = 0
        else:
            return
        win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER,
                             int(value / 100 * 255))
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
        elif 'what is your name' in query:
            speak("I'm your assistant.")
        elif 'who is' in query:
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
        elif any(op in query for op in ['+', '-', '*', '/']):
            result = calculate(query)
            if result is not None:
                speak(f"The result of {query} is {result}")
                print(f"The result of {query} is {result}")
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
            send_email(sender_email, sender_password, receiver_email, subject, body)
            speak("Email sent successfully.")
        elif 'weather in' in query:
            city = query.replace('weather in', '').strip()
            weather_report = get_weather(city)
            speak(weather_report)
            print(weather_report)
        elif 'where am i' in query:
            ip_address = requests.get('https://api.ipify.org').text
            city, region = get_location_from_ip(ip_address)
            if city and region:
                speak(f"Your current location is {city}, {region}.")
            else:
                speak("Sorry, I couldn't determine your location.")
        elif 'translate' in query:
            try:
                speak("Which language would you like to translate to? For example, type 'French', 'Spanish', etc.")
                dest_language = listen().lower()
                dest_language_code = {
                    'english': 'en',
                    'french': 'fr',
                    'spanish': 'es',
                    'german': 'de',
                    'italian': 'it',
                    'portuguese': 'pt',
                    'russian': 'ru'
                }.get(dest_language, 'en')

                speak("What text would you like to translate?")
                text_to_translate = listen()

                translated_text = translate_text(text_to_translate, dest_language_code)
                speak(f"The translation is: {translated_text}")
                print(f"Translation: {translated_text}")
            except Exception as e:
                speak("Sorry, I couldn't perform the translation.")
                print(f"Error during translation: {e}")
        elif 'brightness' in query:
            if 'high' in query:
                set_brightness('high')
                speak("Brightness set to high.")
            elif 'medium' in query:
                set_brightness('medium')
                speak("Brightness set to medium.")
            elif 'low' in query:
                set_brightness('low')
                speak("Brightness set to low.")
        elif 'volume' in query:
            if 'high' in query:
                set_volume('high')
                speak("Volume set to high.")
            elif 'medium' in query:
                set_volume('medium')
                speak("Volume set to medium.")
            elif 'low' in query:
                set_volume('low')
                speak("Volume set to low.")
        elif 'screenshot' in query:
            filename = 'screenshot.png'
            take_screenshot(filename)
            speak("Screenshot taken and saved.")
        else:
            speak("I didn't understand that command. Please try again.")

if __name__ == "__main__":
    run_assistant()

#Credit Kod_Yazarı
