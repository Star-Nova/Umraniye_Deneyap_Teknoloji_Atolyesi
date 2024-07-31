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

def record_and_convert_audio():
    # Recognizer nesnesi oluşturma
    recognizer = sr.Recognizer()

    try:
        # Kullanıcıdan kayıt süresini al
        duration = int(input("How long do you want to record audio for? (in seconds): "))
        print("Starting audio recording from microphone...")

        # Mikrofonla kayıt yap
        with sr.Microphone() as source:
            # Ortam gürültüsüne uyum sağla
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            # Belirtilen süre kadar dinle
            print("You can start talking...")
            audio = recognizer.listen(source, timeout=duration)

        print("Voice recording completed. Converts voice to text...")

        # Google Web Speech API kullanarak ses metne çevir
        text = recognizer.recognize_google(audio, language="en")

        print("Audio transcribed:")
        print(text)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the sound.")
    except sr.RequestError as e:
        print(f"Google Web Speech API service could not be reached; {e}")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"Something went wrong: {e}")
