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

def suggest_popsong():
    try:
        with open('pop_music.txt', 'r') as file:
            pop_music = file.readlines()
            if pop_music:
                pop_musics = random.choice(pop_music).strip()
                return pop_musics
            else:
                return "Pop Music list is empty."
    except FileNotFoundError:
        return "pop_music.txt file not found."

#rock music
def suggest_rocksong():
    try:
        with open('rock_music.txt', 'r') as file:
            rock_music = file.readlines()
            if rock_music:
                rock_musics = random.choice(rock_music).strip()
                return rock_musics
            else:
                return "Rock Music list is empty."
    except FileNotFoundError:
        return "rock_music.txt file not found."

#hippop music
def suggest_hippopsong():
    try:
        with open('hippop_music.txt', 'r') as file:
            hippop_music = file.readlines()
            if hippop_music:
                hippop_musics = random.choice(hippop_music).strip()
                return hippop_musics
            else:
                return "Hip-Pop Music list is empty."
    except FileNotFoundError:
        return "hippop_music.txt file not found."

#country music
def suggest_countrysong():
    try:
        with open('country_music.txt', 'r') as file:
            country_music = file.readlines()
            if country_music:
                country_musics = random.choice(country_music).strip()
                return country_musics
            else:
                return "Country Music list is empty."
    except FileNotFoundError:
        return "country_music.txt file not found."

#jazz music
def suggest_jazzsong():
    try:
        with open('jazz_music.txt', 'r') as file:
            jazz_music = file.readlines()
            if jazz_music:
                jazz_musics = random.choice(jazz_music).strip()
                return jazz_musics
            else:
                return "Jazz Music list is empty."
    except FileNotFoundError:
        return "jazz_music.txt file not found."

#electronik music
def suggest_electroniksong():
    try:
        with open('electronic_music.txt', 'r') as file:
            electronic_music = file.readlines()
            if electronic_music:
                electronic_musics = random.choice(electronic_music).strip()
                return electronic_musics
            else:
                return "Electronic Music list is empty."
    except FileNotFoundError:
        return "electronic_music.txt file not found."

#klasik music
def suggest_kalsikksong():
    try:
        with open('klasic_music.txt', 'r') as file:
            kalsik_music = file.readlines()
            if kalsik_music:
                kalsik_musics = random.choice(kalsik_music).strip()
                return kalsik_musics
            else:
                return "Klasic Music list is empty."
    except FileNotFoundError:
        return "klasic_music.txt file not found."

#latin music
def suggest_latinsong():
    try:
        with open('latin_music.txt', 'r') as file:
            latin_music = file.readlines()
            if latin_music:
                latin_musics = random.choice(latin_music).strip()
                return latin_musics
            else:
                return "Latin Music list is empty."
    except FileNotFoundError:
        return "latin_music.txt file not found."

#folk music
def suggest_folksong():
    try:
        with open('folk_music.txt', 'r') as file:
            folk_music = file.readlines()
            if folk_music:
                folk_musics = random.choice(folk_music).strip()
                return folk_musics
            else:
                return "Latin Music list is empty."
    except FileNotFoundError:
        return "folk_music.txt file not found."