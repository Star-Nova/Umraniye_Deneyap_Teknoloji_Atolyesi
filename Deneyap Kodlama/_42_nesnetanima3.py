from ultralytics import YOLO
import cv2

# Video dosyasını yükleme
img = cv2.imread("zoo.jpg")

# YOLO modelini yükleme
yolo_model = YOLO("yolov8n.pt")

result=yolo_model(img)
annotated_frame = result[0].plot()
cv2.imshow("Nesne tespiti", annotated_frame)
cv2.waitKey(0)
