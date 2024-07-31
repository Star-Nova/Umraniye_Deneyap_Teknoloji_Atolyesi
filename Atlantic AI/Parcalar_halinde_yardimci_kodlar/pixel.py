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
import cv2
import pyttsx3

def get_photo_dimensions(file_path):
    """
    Belirtilen dosyayı okuyarak boyutlarını ekrana ve sesli olarak yazdırır.
    """
    image = cv2.imread(file_path)

    if image is not None:
        height, width = image.shape[:2]
        print(f"Image dimensions: Width: {width}, Height: {height}")
        speak(f"The image dimensions are {width} pixels wide and {height} pixels tall.")
    else:
        print("Unable to read the image file.")
        speak("Unable to read the image file.")

def main():
    # Kullanıcıdan dosya adını al
    file_path = input("Enter the file name (e.g., 'example.png'): ")
    get_photo_dimensions(file_path)