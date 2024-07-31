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

def chat_english():
    speak("Sure, let's chat. How are you today?")
    user_response = listen()

    if user_response in ["good", "fine", "great", "okay"]:
        speak("I'm glad to hear that! What have you been up to lately?")
    elif user_response in ["not good", "bad", "not great"]:
        speak("I'm sorry to hear that. Is there anything specific that's bothering you?")
    else:
        speak("I see. What would you like to talk about today?")

    user_response = listen()
    if "weather" in user_response:
        speak("The weather is quite interesting today. Do you like the current weather?")
    elif "hobbies" in user_response:
        speak("Hobbies are a great way to relax. What hobbies do you enjoy?")
    elif "news" in user_response:
        speak("There are many interesting news stories today. Are you following any particular news?")
    elif "movies" in user_response:
        speak("Movies can be a lot of fun. Do you have a favorite movie or genre?")
    elif "music" in user_response:
        speak("Music is a great way to lift your mood. What kind of music do you like?")
    elif "food" in user_response:
        speak("Food can be so enjoyable. Do you have a favorite dish or type of cuisine?")
    elif "travel" in user_response:
        speak("Traveling opens up new experiences. Where would you like to travel next?")
    elif "books" in user_response:
        speak("Books can be quite engaging. Are you reading any interesting books right now?")
    else:
        speak("That sounds interesting! Is there anything else you'd like to discuss?")
