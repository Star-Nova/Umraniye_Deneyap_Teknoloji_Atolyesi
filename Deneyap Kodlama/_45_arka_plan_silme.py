"""
import cv2
import cvzone
import os
from cvzone.SelfiSegmentationModule import SelfiSegmentation

# Arka plan resimlerini yükleyin ve boyutlandırın
bg = cv2.imread('aa.png')
bg = cv2.resize(bg, (640, 480))

bg2 = cv2.imread("bb.png")
bg2 = cv2.resize(bg2, (640, 480))

bg3 = cv2.imread("cc.png")
bg3 = cv2.resize(bg3, (640, 480))

# Selfi Segmentation objesi oluşturma
seg = SelfiSegmentation()

# Kameradan video yakalama
cap = cv2.VideoCapture(0)

while True:
    read, frame = cap.read()
    if not read:
        break

    # Arka planı kaldırma ve yeni arka plan ekleme
    img1 = seg.removeBG(frame, (0, 0, 0), cutthreshold=0.9)  # Siyah arka plan
    img2 = seg.removeBG(frame, bg, cutthreshold=0.9)         # İlk resim
    img3 = seg.removeBG(frame, bg2, cutthreshold=0.9)        # İkinci resim
    img4 = seg.removeBG(frame, bg3, cutthreshold=0.9)        # Üçüncü resim

    # Görüntüleri birleştir ve göster
    all_frame = cvzone.stackImages([img1, img2, img3, img4], 2, 2, 0.9)
    cv2.imshow("Reklam", all_frame)
    cv2.waitKey(1)

"""
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

# Arka plan resimlerini yükleyin ve boyutlandırın
bg = cv2.imread('aa.png')
bg = cv2.resize(bg, (640, 480)) if bg is not None else None

bg2 = cv2.imread("bb.png")
bg2 = cv2.resize(bg2, (640, 480)) if bg2 is not None else None

bg3 = cv2.imread("cc.png")
bg3 = cv2.resize(bg3, (640, 480)) if bg3 is not None else None

# Selfi Segmentation objesi oluşturma
seg = SelfiSegmentation()

# Kameradan video yakalama
cap = cv2.VideoCapture(0)

while True:
    read, frame = cap.read()
    if not read:
        break

    # Arka planı kaldırma ve yeni arka plan ekleme
    img1 = seg.removeBG(frame, (0, 0, 0), cutthreshold=0.9)  # Siyah arka plan
    img2 = seg.removeBG(frame, bg, cutthreshold=0.9) if bg is not None else frame
    img3 = seg.removeBG(frame, bg2, cutthreshold=0.9) if bg2 is not None else frame
    img4 = seg.removeBG(frame, bg3, cutthreshold=0.9) if bg3 is not None else frame

    # Görüntüleri birleştir ve göster
    all_frame = cvzone.stackImages([img1, img2, img3, img4], 2, 2, 0.9)
    cv2.imshow("Reklam", all_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' tuşuna basıldığında çıkış yap
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
