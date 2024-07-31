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
