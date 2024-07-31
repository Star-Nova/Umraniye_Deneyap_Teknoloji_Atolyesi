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

def suggest_actionfilm():
    try:
        with open('actionfilm.txt', 'r') as file:
            actionfilm = file.readlines()
            if actionfilm:
                actionfilms = random.choice(actionfilm).strip()
                return actionfilms
            else:
                return "Action Film list is empty."
    except FileNotFoundError:
        return "actionfilm.txt file not found."

    #komedi film önerir
def suggest_comedyfilm():
    try:
        with open('comedyfilm.txt', 'r') as file:
            comedyfilm = file.readlines()
            if comedyfilm:
                comedyfilms = random.choice(comedyfilm).strip()
                return comedyfilms
            else:
                return "Comedy film list is empty."
    except FileNotFoundError:
        return "comedyfilm.txt file not found."

    # Drama tarzı film önerir
def suggest_dramafilm():
    try:
        with open('dramafilm.txt', 'r') as file:
            dramafilm = file.readlines()
            if dramafilm:
                dramafilms = random.choice(dramafilm).strip()
                return dramafilms
            else:
                return "Drama Film list is empty."
    except FileNotFoundError:
        return "dramafilm.txt file not found."

    #korku filmi önerir
def suggest_horrorfilm():
    try:
        with open('horrorfilm.txt', 'r') as file:
            horrorfilm = file.readlines()
            if horrorfilm:
                horrorfilms = random.choice(horrorfilm).strip()
                return horrorfilms
            else:
                return "Horror Film list is empty."
    except FileNotFoundError:
        return "horrorfilm.txt file not found."

    #bilim kurgu filmi önerir
def suggest_science_fiction_film():
    try:
        with open('sciencefictionfilm.txt', 'r') as file:
            science_fiction_film = file.readlines()
            if science_fiction_film:
                science_fiction_films = random.choice(science_fiction_film).strip()
                return science_fiction_films
            else:
                return "Science fiction film list is empty."
    except FileNotFoundError:
        return "sciencefictionfilm.txt file not found."

    #romantik tarzı filmler önerir
def suggest_romantic_film():
    try:
        with open('romanticfilm.txt', 'r') as file:
            romantic_film = file.readlines()
            if romantic_film:
                romantic_films = random.choice(romantic_film).strip()
                return romantic_films
            else:
                return "Romantic Film list is empty."
    except FileNotFoundError:
        return "romanticfilm.txt file not found."

   #Belgesel tarzı
def suggest_documentary_film():
    try:
        with open('documentaryfilm.txt', 'r') as file:
            documentary_film = file.readlines()
            if documentary_film:
                documentary_films = random.choice(documentary_film).strip()
                return documentary_films
            else:
                return "Documentary Film list is empty."
    except FileNotFoundError:
        return "documentaryfilm.txt file not found."

    #animasyon tarzı film
def suggest_animation_film():
    try:
        with open('animationfilm.txt', 'r') as file:
            animation_film = file.readlines()
            if animation_film:
                animation_films = random.choice(animation_film).strip()
                return animation_films
            else:
                return "Animation Film list is empty."
    except FileNotFoundError:
        return "animationfilm.txt file not found."

    #tarihi film
def suggest_historic_film():
    try:
        with open('historicfilm.txt', 'r') as file:
            historic_film = file.readlines()
            if historic_film:
                historic_films = random.choice(historic_film).strip()
                return historic_films
            else:
                return "Historical Film list is empty."
    except FileNotFoundError:
        return "historicfilm.txt file not found."
