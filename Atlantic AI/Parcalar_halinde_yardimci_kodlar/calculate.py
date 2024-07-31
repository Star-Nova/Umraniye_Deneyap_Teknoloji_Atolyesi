import os
import pyautogui
import wavio
from gtts import gTTS
import os
import sounddevice as sd
import datetime
from twilio.rest import Client
import cv2
import pyttsx3

import httpx
import math
import speech_recognition as sr
import sounddevice as sd
import speech_recognition as sr
import speech_recognition as sr
import numpy as np
import speech_recognition_python
import wavio
import platform
import pyautogui
import pyttsx3
from PIL import Image, ImageDraw,ImageFont
import cv2
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
from gtts import gTTS
import os
import sounddevice as sd
import wavio
import math

def calculate(query):
    try:
        # İşlemleri daha karmaşık hale getirmek için değerlendirme yapıyoruz
        result = eval(query)
        return result
    except Exception as e:
        print(f"Error calculating expression: {e}")
        return None
def handle_math_query(query):
    # Python'un desteklediği çeşitli matematik işlemlerini kontrol et
    operations = ['+', '-', '*', '/', '**', '//', '%', 'sqrt', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'exp', 'ceil', 'floor', 'fabs', 'factorial', 'gcd', 'pow']

    # Sorgunun içerisinde bir işlem olup olmadığını kontrol et
    if any(op in query for op in operations):
        # Parantez içi ifadeleri çözerek işlemi daha güvenli hale getirin
        query = query.replace('sqrt','math.sqrt')  # Karekök hesaplamak için, math.sqrt fonksiyonunu kullanır
        query = query.replace('sin','math.sin')  # Sinüs hesaplamak için, math.sin fonksiyonunu kullanır
        query = query.replace('cos','math.cos')  # Kosinüs hesaplamak için, math.cos fonksiyonunu kullanır
        query = query.replace('tan','math.tan')  # Tanjant hesaplamak için, math.tan fonksiyonunu kullanır
        query = query.replace('asin','math.asin')  # Ark sinüs hesaplamak için, math.asin fonksiyonunu kullanır
        query = query.replace('acos','math.acos')  # Ark kosinüs hesaplamak için, math.acos fonksiyonunu kullanır
        query = query.replace('atan','math.atan')  # Ark tanjant hesaplamak için, math.atan fonksiyonunu kullanır
        query = query.replace('log','math.log')  # Logaritma hesaplamak için, math.log fonksiyonunu kullanır (doğal logaritma)
        query = query.replace('exp','math.exp')  # Üstel (exponential) fonksiyonunu hesaplamak için, math.exp fonksiyonunu kullanır
        query = query.replace('ceil','math.ceil')  # Yukarı yuvarlama yapmak için, math.ceil fonksiyonunu kullanır
        query = query.replace('floor','math.floor')  # Aşağı yuvarlama yapmak için, math.floor fonksiyonunu kullanır
        query = query.replace('fabs','math.fabs')  # Mutlak değeri hesaplamak için, math.fabs fonksiyonunu kullanır
        query = query.replace('factorial','math.factorial')  # Faktöriyel hesaplamak için, math.factorial fonksiyonunu kullanır
        query = query.replace('gcd','math.gcd')  # İki sayının en büyük ortak bölenini bulmak için, math.gcd fonksiyonunu kullanır
        query = query.replace('pow','math.pow')  # Üs alma işlemi için, math.pow fonksiyonunu kullanır

        result = calculate(query)

        if result is not None:
            speak(f"The result of {query} is {result}")
            print(f"The result of {query} is {result}")
        else:
            speak("Sorry, I couldn't calculate that expression.")
            print("Sorry, I couldn't calculate that expression.")
    else:
        speak("No recognizable mathematical operation found.")
        print("No recognizable mathematical operation found.")



