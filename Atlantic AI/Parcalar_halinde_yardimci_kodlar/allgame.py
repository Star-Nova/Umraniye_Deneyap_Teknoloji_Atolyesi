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