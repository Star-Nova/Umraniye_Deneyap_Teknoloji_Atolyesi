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

def suggest_dessert():
    try:
        with open('Desserts.txt', 'r') as file:
            desserts = file.readlines()
            if desserts:
                dessert = random.choice(desserts).strip()
                webbrowser.open(f"https://www.youtube.com/results?search_query={dessert}")
                return dessert
            else:
                return "Dessert list is empty."
    except FileNotFoundError:
        return "Desserts.txt file not found."


def suggest_meatdishes():
    try:
        with open('meatdishes.txt', 'r') as file:
            meatdishes = file.readlines()
            if meatdishes:
                meatdish = random.choice(meatdishes).strip()
                return meatdish
            else:
                return "Meat Dishes list is empty."
    except FileNotFoundError:
        return "meatdishes.txt file not found."


def suggest_vegetabledishes():
    try:
        with open('vegetabledishes.txt', 'r') as file:
            vegetabledishes = file.readlines()
            if vegetabledishes:
                vegetabledish = random.choice(vegetabledishes).strip()
                return vegetabledish
            else:
                return "Vegetable Dishes list is empty."
    except FileNotFoundError:
        return "vegetabledishes.txt file not found."


def suggest_soup():
    try:
        with open('soup.txt', 'r') as file:
            soups = file.readlines()
            if soups:
                soup = random.choice(soups).strip()
                return soup
            else:
                return "Soup list is empty."
    except FileNotFoundError:
        return "soup.txt file not found."


def suggest_bread():
    try:
        with open('bread.txt', 'r') as file:
            breads = file.readlines()
            if breads:
                bread = random.choice(breads).strip()
                return bread
            else:
                return "Bread list is empty."
    except FileNotFoundError:
        return "bread.txt file not found."


def suggest_salad():
    try:
        with open('salad.txt', 'r') as file:
            salads = file.readlines()
            if salads:
                salad = random.choice(salads).strip()
                return salad
            else:
                return "Salad list is empty."
    except FileNotFoundError:
        return "salad.txt file not found."


def suggest_hamurisleri():
    try:
        with open('hamurisleri.txt', 'r') as file:
            hamurisleri = file.readlines()
            if hamurisleri:
                hamur = random.choice(hamurisleri).strip()
                return hamur
            else:
                return "Hamur işleri listesi boş."
    except FileNotFoundError:
        return "hamurisleri.txt dosyası bulunamadı."


def suggest_icecream():
    try:
        with open('icecream.txt', 'r') as file:
            icecreams = file.readlines()
            if icecreams:
                icecream = random.choice(icecreams).strip()
                return icecream
            else:
                return "Ice cream list is empty."
    except FileNotFoundError:
        return "icecream.txt file not found."