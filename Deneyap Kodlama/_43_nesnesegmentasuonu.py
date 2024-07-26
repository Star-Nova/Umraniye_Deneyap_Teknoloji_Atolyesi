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

# Video yazıcısı oluşturun
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
output = cv2.VideoWriter("trafikseg.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))

while True:
    read, frame = cap.read()
    if read:
        # YOLO modeliyle çerçeveyi işleyin
        result = yolo_model.predict(frame)

        # Annotator sınıfından bir örnek oluşturun
        annotate_frame = Annotator(frame, line_width=2, font_size=12, font="ARIAL")

        if result[0].masks is not None:
            clss = result[0].boxes.cls.cpu().tolist()
            masks = result[0].masks.xy

            # Her maske ve sınıf için sınırlayıcı kutu ve etiket uygulayın
            for mask, clas in zip(masks, clss):
                points = np.array(mask,dtype=np.int32)
                cv2.fillPoly(frame,[points],color=(0,255,0))

                annotate_frame.seg_bbox(mask=mask, mask_color=colors(int(clas)), det_label=names[int(clas)])

        # İşlenmiş çerçeveyi video dosyasına yazın
        output.write(frame)

        # İşlenmiş çerçeveyi gösterin
        cv2.imshow("Segmentasyon", frame)

        # Çıkış için q tuşuna basılmasını bekleyin
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Kaynakları serbest bırakın ve pencereleri kapatın
cap.release()
output.release()
cv2.destroyAllWindows()