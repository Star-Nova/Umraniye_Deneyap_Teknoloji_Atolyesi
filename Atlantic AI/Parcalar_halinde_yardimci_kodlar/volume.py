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