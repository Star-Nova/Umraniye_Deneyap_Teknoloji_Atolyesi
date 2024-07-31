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