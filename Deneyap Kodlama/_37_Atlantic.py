"""
import time
import pywhatkit
import speech_recognition as sr
import os
import wikipedia
from gtts import gTTS
import pyjokes
from playsound import playsound

listener = sr.Recognizer()

def talk(text):
    data = gTTS(text=text, lang="en")
    data.save("Atlantic.mp3")
    playsound("Atlantic.mp3")
    os.remove("Atlantic.mp3")

def input_data(): # benim sesli komut girmem
    with sr.Microphone() as mic:
        listener.adjust_for_ambient_noise(mic)
        print("Listening ...")
        audio = listener.listen(mic)
        try:
            text = listener.recognize_google(audio)
            text = text.lower()
            if "Hello Atlantic" in text:
                text = text.replace("Hello Atlantic", "") # Chat GTP5 yazısını siler
                print(text)
                return str(text)
            else:
                print("Atlantic not found")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, my speech service is down.")
        return ""

def Atlantic():
    talk("Hi, I am Atlantic. How can I help you?")
    while True:
        text = input_data()
        if text:
            if "sign out" in text:
                talk("Signing out. Goodbye!")
                break
            elif "play" in text:
                song = text.replace("play", "")
                pywhatkit.playonyt(song)
            elif "jokes" in text:
                joke = pyjokes.get_joke()
                print(joke)
                talk(joke)
            elif "how are you" in text:
                talk("Thanks, bro.")
            elif "what is your name" in text:
                talk("Atlantic")
            elif "who" in text:
                human = text.replace("who", "")
                info = wikipedia.summary(human, 1)
                print(info)
                talk(info)
            elif "search" in text:
                search = text.replace("search", "")
                pywhatkit.search(search)
                talk("Searching..." + search)

Atlantic()
"""
#Atlantic4o a.i

import os
import wikipedia
import webbrowser
import pyttsx3
import speech_recognition as sr
import smtplib, ssl
import requests
import pyjokes
import time
import cv2
import mediapipe as mp

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # İsterseniz ses seçimini buradan ayarlayabilirsiniz.

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
    # Belirli anahtar kelimeleri kaldırmak için fonksiyon
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
    port = 587  # SSL için 465, TLS için 587

    message = f"Subject: {subject}\n\n{body}"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

def get_location_from_ip(ip_address):
    ipstack_api_key = "YOUR_IPSTACK_API_KEY"  # IPStack API anahtarınızı buraya ekleyin
    base_url = f"http://api.ipstack.com/{ip_address}?access_key={ipstack_api_key}"

    response = requests.get(base_url)
    data = response.json()

    if 'city' in data and 'region_name' in data:
        city = data['city']
        region = data['region_name']
        return city, region
    else:
        return None, None

def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # OpenWeatherMap API anahtarınızı buraya ekleyin
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

def open_camera_and_detect_hand():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.imshow('Hand Tracking', image)

            if cv2.waitKey(5) & 0xFF == 27:  # Press 'Esc' to exit
                break

    cap.release()
    cv2.destroyAllWindows()

def run_assistant():
    speak("Hi, I'm your assistant. My name is Atlantic. How can I help you today?")
    while True:
        query = listen()
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
        elif 'open the camera' in query:
            speak("Opening the camera.")
            open_camera_and_detect_hand()
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

            try:
                send_email(sender_email, sender_password, receiver_email, subject, body)
                speak("Email sent successfully.")
            except Exception as e:
                speak(f"Sorry, I couldn't send the email. Error: {e}")

        elif 'weather' in query:
            ip_address = "YOUR_IP_ADDRESS"  # Belirtilen IP adresini burada kullanıyoruz
            city, region = get_location_from_ip(ip_address)
            if city and region:
                weather_report = get_weather(city)
                speak(weather_report)
                print(weather_report)
            else:
                speak("Sorry, I couldn't determine the location from the IP address.")

        if __name__ == "__main__":
            run_assistant()



#Credit Kod_Yazarı