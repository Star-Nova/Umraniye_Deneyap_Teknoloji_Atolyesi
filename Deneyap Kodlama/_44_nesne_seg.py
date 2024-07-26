"""

import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

# YOLO modelini yükleyin
yolo_model = YOLO("yolov8n-seg.pt")

# Video yakalama
cap = cv2.VideoCapture("trafic1.mp4")
names = yolo_model.names
print(names)

while True:
    read, frame = cap.read()
    if read:
        # YOLO modeliyle çerçeveyi işleyin
        result = yolo_model.predict(frame)

        # Annotator sınıfından bir örnek oluşturun
        ann=Annotator(frame)
        if result[0].masks is not None:
            clss=result[0].boxes.cls.cpu().tolist()
            masks=result[0].masks.xy
            for mask,cls in zip(masks,clss):
                ann.seg_bbox(mask=mask, mask_color=colors(int(clas)), det_label=names[int(clas)])

    cv2.imshow("Segment",frame)
    cv2.waitKey(1)

"""
import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

# YOLO modelini yükleyin
yolo_model = YOLO("yolov8n-seg.pt")

# Video yakalama
cap = cv2.VideoCapture("trafic1.mp4")
names = yolo_model.names  # YOLO modelinden sınıf isimlerini al
print(names)

while True:
    read, frame = cap.read()  # Çerçeveyi oku
    if not read:  # Eğer okuma başarılı değilse
        break  # Döngüyü sonlandır

    # YOLO modeliyle çerçeveyi işleyin
    results = yolo_model.predict(frame)  # Sonuçları alın

    # Annotator sınıfından bir örnek oluşturun
    ann = Annotator(frame)
    if results[0].masks is not None:  # Maskeler varsa
        clss = results[0].boxes.cls.cpu().tolist()  # Sınıf etiketlerini al
        masks = results[0].masks.xy  # Maskeleri al

        for mask, cls in zip(masks, clss):
            # `seg_bbox` fonksiyonunda kullanılan parametrelerin doğruluğunu kontrol edin
            ann.seg_bbox(mask=mask, mask_color=colors(int(cls)), det_label=names[int(cls)])

    cv2.imshow("Segment", frame)  # İşlenmiş çerçeveyi göster
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' tuşuna basıldığında çıkış yap
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
