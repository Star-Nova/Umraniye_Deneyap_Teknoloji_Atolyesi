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

def make_call():
    # Kullanıcıdan Twilio bilgilerini ve telefon numaralarını al
    twilio_sid = input("Twilio SID'nizi girin: ")
    twilio_auth_token = input("Twilio Auth Token'nınızı girin: ")
    from_phone_number = input("Kendi telefon numaranızı (Twilio'dan aldığınız) girin: ")
    to_phone_number = input("Aramak istediğiniz telefon numarasını girin: ")

    # Twilio client'ını oluştur
    client = Client(twilio_sid, twilio_auth_token)

    # Arama yap
    try:
        call = client.calls.create(
            to=to_phone_number,
            from_=from_phone_number,
            url="http://demo.twilio.com/docs/voice.xml"  # Bu URL, arama sırasında çalınacak ses dosyasının URL'sidir
        )
        print(f'Arama yapıldı, SID: {call.sid}')
    except Exception as e:
        print(f"Arama sırasında bir hata oluştu: {str(e)}")
