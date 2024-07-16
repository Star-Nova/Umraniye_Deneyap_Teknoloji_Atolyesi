import os
import requests as req
import cv2
import numpy as np
import mediapipe as mp

video=cv2.VideoCapture(0)  #Kameramızın çalışmasını sağlar
m= mp.solutions.hands
hands=m.Hands()
draw=mp.solutions.drawing_utils #landmarks ( noktalar arası)'lar arası çizimler için fonksiyon
video.set(4,250) #Videonun boyutunu ayarlar
video.set(3,250) #Videonun boyutunu ayarlar
while True:
    succes,frame=video.read()
    frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #RENK KODUNU RGBYE ÇEVİRİR
    result=hands.process(frame_rgb) #hands classı ile eller algılanır
    print(result.multi_hand_landmarks) #algılanan ellerin x,y,z değerlerini ekrana yazdırır.
    if result.multi_hand_landmarks: #ekrana el gördüğü zaman çalışması için
        for handlm in result.multi_hand_landmarks: #her bir landmark için çizimi için
            draw.draw_landmarks(frame,#nereyi çizim yapacağını
                                handlm, #her bir el içi 21lik landmark seti
                                mp.solutions.hands.HAND_CONNECTIONS, #landmarklar arasındaki çizgiler
                                mp.solutions.drawing_utils.DrawingSpec(color=(0,0,0)), #noktaların renkleri
                                mp.solutions.drawing_utils.DrawingSpec(color=(0,0,0)) #çizgilerin renkleri
                                )
            for id, lm in enumerate(handlm.landmark):
                print(id,lm) #Bir elin için her landmarkın idsini ve değerini verir
                h,w,c=frame.shape
                x,y=int(lm.x*w),int(lm.y*h) #landmarkların ekrandaki hangi pixele denk geleceğini belirtir
                print(id," ",x," ",y)

                if id == 4:  # Baş parmağın ucu
                    x1,y1 = x, y
                    cv2.circle(frame, (x, y), 8, (0, 0, 0), cv2.FILLED)


                if id==8:
                    x2,y2 = x, y
                    cv2.circle(frame, (x, y), 8, (0, 0, 0), cv2.FILLED)
                    cv2.line(frame,(x1,y1),(x2,y2),(0,0,0),4)


    cv2.imshow("Hand Detection",frame)
    cv2.waitKey(1) #Her milisaniyede bir görüntü değişiyor.

