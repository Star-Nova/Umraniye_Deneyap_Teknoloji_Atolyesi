from ultralytics import YOLO
import cv2

# Video dosyasını yükleme
cap = cv2.VideoCapture("trafic3.mp4")

# YOLO modelini yükleme
yolo_model = YOLO("yolov8n.pt")

while cap.isOpened():
    read, frame = cap.read()
    if read:
        # Modeli kare üzerinde çalıştırma
        results = yolo_model(frame)

        # Tespit edilen karelerin etrafını çizen ve sınıf adlarını yazan fonksiyon
        annotated_frame = results[0].plot()

        # İşlenmiş çerçeveyi gösterme
        cv2.imshow("Yolo_Traffic", annotated_frame)

        # Çerçeve başına bir anahtar basımı bekler
        cv2.waitKey(1)


# Videoyu durdurur
cap.release()
# Bütün pencereleri kapatır
cv2.destroyAllWindows()
