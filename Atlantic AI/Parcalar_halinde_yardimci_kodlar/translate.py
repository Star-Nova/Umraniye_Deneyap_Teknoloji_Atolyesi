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


def atlantictranslatemod():
    print("Language Selection Menu:")
    print("1. Türkçe")
    print("2. English")
    print("3. Español")
    print("4. Русский (Russian)")
    print("5. Italiano")
    print("6. Français")
    print("7. 中文 (Chinese)")
    print("8. 한국어 (Korean)")
    print("9. Português (Portuguese)")
    print("10. 日本語 (Japanese)")
    print("11. العربية (Arabic)")
    print("12. हिन्दी (Hindi)")
    print("13. Kiswahili (Swahili)")
    print("14. Svenska (Swedish)")
    print("15. Dansk (Danish)")
    print("16. Deutsch (German)")
    print("17. বাংলা (Bengali)")
    print("18. فارسی (Farsi)")
    print("19. Javanese")
    print("20. Catalan")
    print("21. Croatian")
    print("22. Czech")
    print("23. Serbian")
    print("24. Polish")
    print("25. Hungarian")
    print("26. Malay")
    print("27. Filipino")
    print("28. Vietnamese")
    print("29. Nepali")
    print("30. Thai")
    print("31. Slovak")
    print("32. Burmese")
    print("33. Albanian")
    print("34. Macedonian")
    print("35. Estonian")
    print("36. Latvian")
    print("37. Lithuanian")
    print("38. Icelandic")
    print("39. Manx")
    print("40. Welsh")
    print("41. Slovenian")
    print("42. Mongolian")
    print("43. Somali")
    print("44. Kurdish")
    print("45. Punjabi")
    print("46. Tatar")
    print("47. Yiddish")
    print("48. Hawaiian")
    print("49. Samoan")
    print("50. Maltese")
    print("51. Belarusian")
    print("52. Uighur")
    print("53. Kazakh")
    print("0. Exit")

    lang_map = {
        "1": "tr",
        "2": "en",
        "3": "es",
        "4": "ru",
        "5": "it",
        "6": "fr",
        "7": "zh-CN",
        "8": "ko",
        "9": "pt",
        "10": "ja",
        "11": "ar",
        "12": "hi",
        "13": "sw",
        "14": "sv",
        "15": "da",
        "16": "de",  # Added German
        "17": "bn",
        "18": "fa",
        "19": "jv",
        "20": "ca",
        "21": "hr",
        "22": "cs",
        "23": "sr",
        "24": "pl",
        "25": "hu",
        "26": "ms",
        "27": "tl",
        "28": "vi",
        "29": "ne",
        "30": "th",
        "31": "sk",
        "32": "my",
        "33": "sq",
        "34": "mk",
        "35": "et",
        "36": "lv",
        "37": "lt",
        "38": "is",
        "39": "gmh",
        "40": "cy",
        "41": "sl",
        "42": "mn",
        "43": "so",
        "44": "ku",
        "45": "pa",
        "46": "tt",
        "47": "yi",
        "48": "haw",
        "49": "sm",
        "50": "mt",
        "51": "be",
        "52": "ug",
        "53": "kk"
    }

    while True:
        choice = input("Please select a language by entering the corresponding number (0 to exit): ")

        if choice == "0":
            print("Exiting the program. Goodbye!")
            break

        lang = lang_map.get(choice)

        if not lang:
            print("Lütfen geçerli bir dil seçiniz.")
            continue

        text = input("Enter the text you want to convert to speech:\n")

        try:
            translate = gTTS(text=text, lang=lang)  # Convert text to speech
            file_name = "texttospeech.mp3"
            translate.save(file_name)  # Save the audio file

            print("Playing the converted speech...")
            os.system(file_name)  # Play the audio file

            # Option to replay or delete the file
            while True:
                replay = input("Do you want to replay the audio? (yes/no): ").strip().lower()
                if replay == 'yes':
                    os.system(file_name)
                elif replay == 'no':
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            # Clean up: Option to delete the file after use
            cleanup = input("Do you want to delete the audio file? (yes/no): ").strip().lower()
            if cleanup == 'yes':
                os.remove(file_name)
                print("Audio file deleted.")

        except Exception as e:
            print(f"An error occurred: {e}")
