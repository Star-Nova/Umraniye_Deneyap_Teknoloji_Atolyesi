"""
import time
import wave
import struct
import threading
from pynput import keyboard
from pvrecorder import PvRecorder

import torch
import torchaudio
from transformers import AutoProcessor, AutoModelForCTC


class SesKaydedici:
    def __init__(self):
        self.ses = []
        self.is_parcacigi = None
        self.kaydedici = PvRecorder(frame_length=512)

        self.processor = AutoProcessor.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-turkish")
        self.model = AutoModelForCTC.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-turkish")

    def ses_kaydet(self):
        print("Kayıt başlatılıyor")
        self.kaydedici.start()
        while self.kaydedici.is_recording:
            self.ses.extend(self.kaydedici.read())
        # print(self.ses)
        with wave.open("ses.wav", 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(self.ses), *self.ses))
        self.ses = []
        print("Kayıt bitti")

    def on_press(self, key):
        try:
            if key.char == 'a' and self.is_parcacigi is None:
                self.is_parcacigi = threading.Thread(
                    target=self.ses_kaydet,
                    args=(),
                    daemon=True
                )
                self.is_parcacigi.start()
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            if key == keyboard.Key.esc:
                print("Çıkış yapılıyor.")
                return False

            if key.char == 'a':
                self.kaydedici.stop()
                self.is_parcacigi = None
                time.sleep(1)
                self.texte_cevir()
        except AttributeError:
            pass

    def texte_cevir(self):
        waveform, sample_rate = torchaudio.load("ses.wav")
        waveform_resampled = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(waveform)
        with torch.no_grad():
            logits = self.model(waveform_resampled).logits

        # argmax'a bak
        output_ids = torch.argmax(logits, dim=-1)
        command = self.processor.batch_decode(output_ids)

        print("Komutunuz:", command)

    def baslat(self):
        with keyboard.Listener(
                suppress=True,
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()


# if __name__ == "__main__":
kaydedici = SesKaydedici()
print("Kayit modu hazir")
kaydedici.baslat()


import os
import requests as req
import cv2
import numpy as np
import mediapipe as mp


import threading
import time
import cv2
from pynput import keyboard

class SesKaydedici:
    def __init__(self):
        self.ses = []
        self.is_parcacigi = None
        self.kaydedici = PvRecorder(frame_length=512)

        self.processor = AutoProcessor.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-turkish")
        self.model = AutoModelForCTC.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-turkish")

    def ses_kaydet(self):
        print("Kayıt başlatılıyor")
        self.kaydedici.start()
        while self.kaydedici.is_recording:
            self.ses.extend(self.kaydedici.read())
        # print(self.ses)
        with wave.open("ses.wav", 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(self.ses), *self.ses))
        self.ses = []
        print("Kayıt bitti")

    def on_press(self, key):
        try:
            if key.char == 'a' and self.is_parcacigi is None:
                self.is_parcacigi = threading.Thread(
                    target=self.ses_kaydet,
                    args=(),
                    daemon=True
                )
                self.is_parcacigi.start()
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            if key == keyboard.Key.esc:
                print("Çıkış yapılıyor.")
                return False

            if key.char == 'a':
                self.kaydedici.stop()
                self.is_parcacigi = None
                time.sleep(1)
                self.texte_cevir()
        except AttributeError:
            pass



        video=cv2.VideoCapture(0)
        m= mp.solutions.hands
        hands=m.Hands()
        draw=mp.solutions.drawing_utils
        video.set(4,250)
        video.set(3,250)
        while True:
            succes,frame=video.read()
            frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            result=hands.process(frame_rgb)
            print(result.multi_hand_landmarks)
            if result.multi_hand_landmarks:
                for handlm in result.multi_hand_landmarks:
                    draw.draw_landmarks(frame,
                                        handlm,
                                        mp.solutions.hands.HAND_CONNECTIONS,
                                        mp.solutions.drawing_utils.DrawingSpec(color=(0,0,0)),
                                        mp.solutions.drawing_utils.DrawingSpec(color=(0,0,0))
                                        )
                    for id, lm in enumerate(handlm.landmark):
                        print(id,lm)
                        h,w,c=frame.shape
                        x,y=int(lm.x*w),int(lm.y*h)
                        print(id," ",x," ",y)

                        if id == 4:
                            x1,y1 = x, y
                            cv2.circle(frame, (x, y), 8, (0, 0, 0), cv2.FILLED)


                        if id==8:
                            x2,y2 = x, y
                            cv2.circle(frame, (x, y), 8, (0, 0, 0), cv2.FILLED)
                            cv2.line(frame,(x1,y1),(x2,y2),(0,0,0),4)


            cv2.imshow("Hand Detection",frame)
            cv2.waitKey(1)

"""
"""
import time
import wave
import struct
import threading
from pynput import keyboard
from pvrecorder import PvRecorder

import torch
import torchaudio
from transformers import AutoProcessor, AutoModelForCTC
import cv2

class SesKaydedici:
    def __init__(self):
        self.ses = []
        self.is_parcacigi = None
        self.kaydedici = PvRecorder(frame_length=512)

        self.processor = AutoProcessor.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-turkish")
        self.model = AutoModelForCTC.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-turkish")

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def ses_kaydet(self):
        print("Kayıt başlatılıyor")
        self.kaydedici.start()
        while self.kaydedici.is_recording:
            self.ses.extend(self.kaydedici.read())

        with wave.open("ses.wav", 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(self.ses), *self.ses))
        self.ses = []
        print("Kayıt bitti")

    def yuz_tani(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow('Yuz Tanima', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def on_press(self, key):
        try:
            if key.char == 'a' and self.is_parcacigi is None:
                self.is_parcacigi = threading.Thread(
                    target=self.ses_kaydet,
                    args=(),
                    daemon=True
                )
                self.is_parcacigi.start()

            elif key.char == 'b' and self.is_parcacigi is None:
                self.is_parcacigi = threading.Thread(
                    target=self.yuz_tani,
                    args=(),
                    daemon=True
                )
                self.is_parcacigi.start()

        except AttributeError:
            pass

    def on_release(self, key):
        try:
            if key == keyboard.Key.esc:
                print("Çıkış yapılıyor.")
                return False

            if key.char == 'a' or key.char == 'b':
                self.kaydedici.stop()
                self.is_parcacigi = None
                time.sleep(1)
                if key.char == 'a':
                    self.texte_cevir()

        except AttributeError:
            pass

    def texte_cevir(self):
        waveform, sample_rate = torchaudio.load("ses.wav")
        waveform_resampled = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(waveform)

        with torch.no_grad():
            logits = self.model(waveform_resampled).logits

        output_ids = torch.argmax(logits, dim=-1)
        command = self.processor.batch_decode(output_ids)

        print("Komutunuz:", command)

    def baslat(self):
        with keyboard.Listener(
                suppress=True,
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    kaydedici = SesKaydedici()
    print("Kayıt modu hazır")
    kaydedici.baslat()
"""
import time
import wave
import struct
import threading
from pynput import keyboard
from pvrecorder import PvRecorder

import torch
import torchaudio
from transformers import AutoProcessor, AutoModelForCTC
import cv2

class SesKaydedici:
    def __init__(self):
        self.ses = []
        self.is_parcacigi = None
        self.kaydedici = PvRecorder(frame_length=512)

        self.processor = AutoProcessor.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-turkish")
        self.model = AutoModelForCTC.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-turkish")

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def ses_kaydet(self):
        print("Kayıt başlatılıyor")
        self.kaydedici.start()
        while self.kaydedici.is_recording:
            self.ses.extend(self.kaydedici.read())

        with wave.open("ses.wav", 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(self.ses), *self.ses))
        self.ses = []
        print("Kayıt bitti")

    def yuz_tani(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow('Yuz Tanima', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def on_press(self, key):
        try:
            if key.char == 'a' and self.is_parcacigi is None:
                self.is_parcacigi = threading.Thread(
                    target=self.ses_kaydet,
                    args=(),
                    daemon=True
                )
                self.is_parcacigi.start()

            elif key.char == 'b' and self.is_parcacigi is None:
                self.is_parcacigi = threading.Thread(
                    target=self.yuz_tani,
                    args=(),
                    daemon=True
                )
                self.is_parcacigi.start()

        except AttributeError:
            pass

    def on_release(self, key):
        try:
            if key == keyboard.Key.esc:
                print("Çıkış yapılıyor.")
                return False

            if key.char == 'a' or key.char == 'b':
                self.kaydedici.stop()
                self.is_parcacigi = None
                time.sleep(1)
                if key.char == 'a':
                    self.texte_cevir()

        except AttributeError:
            pass

    def texte_cevir(self):
        waveform, sample_rate = torchaudio.load("ses.wav")
        waveform_resampled = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(waveform)

        with torch.no_grad():
            logits = self.model(waveform_resampled).logits

        output_ids = torch.argmax(logits, dim=-1)
        command = self.processor.batch_decode(output_ids)

        print("Komutunuz:", command)

    def baslat(self):
        with keyboard.Listener(
                suppress=True,
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    kaydedici = SesKaydedici()
    print("Kayıt modu hazır")
    kaydedici.baslat()
osaslipt

