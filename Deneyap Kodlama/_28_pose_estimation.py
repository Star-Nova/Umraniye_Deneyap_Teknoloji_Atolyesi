import os
import requests as req
import cv2
import numpy as np

"""

image_url = "https://raw.githubusercontent.com/quanhua92/human-pose-estimation-opencv/master/image.jpg"
model_url = 'https://raw.githubusercontent.com/quanhua92/human-pose-estimation-opencv/master/graph_opt.pb'


if not os.path.exists('image.jpg'):
    img = req.get(image_url).content
    with open('image.jpg','wb') as fd:
        fd.write(img)

if not os.path.exists('graph_opt.pb'):
    model = req.get(model_url).content
    with open('graph_opt.pb', 'wb') as fd:
        fd.write(model)


BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
               "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
               ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

model=cv2.dnn.readNetFromTensorflow("graph_opt.pb")
img=cv2.imread("image.jpg")
print(img.shape)
print(img[0]) #Blue kanalını verir

f_w,f_h=img.shape[:2] #görüntünün genişliğini ve yüksekliğini verir.
print(f_w,f_h)
blob=cv2.dnn.blobFromImage(img,1,(f_w,f_h),swapRB=True,crop=False)
print(blob.shape)
print(blob[0,0])
model.setInput(blob)
detect=model.forward()
print(detect)
print(detect.shape)
detect=detect[:,:19,:,:]
print(detect.shape)
points=[]

for i in range(len(BODY_PARTS)):
    heatMap=detect[0,i,:,:]
    _,conf,_,maxloc=cv2.minMaxLoc(heatMap)
    x=(f_w * maxloc[0]) / detect.shape[3]
    y = (f_h * maxloc[1]) / detect.shape[2]
    if conf > 0.25:
        points.append((x,y))
    else:
        points.append(None)

print(f"points :{points}")

for pair in POSE_PAIRS:
    partFrom=pair[0]
    partTo=pair[1]
    assert (partTo in BODY_PARTS)
    assert (partFrom in BODY_PARTS)

    idFrom=BODY_PARTS[partFrom]
    idTo=BODY_PARTS[partTo]

    if points[idFrom] and points[idTo]:
        cv2.line(img,points[idFrom],points[idTo],(0,0,255),3)
        #cv2.ellipse(img,points[idFrom],(3,3),0,0,360,(0,0,255),cv2.FILLED)
        #cv2.ellipse(img,points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv2.FILLED) #cv2.FILLED içini doldurmayı sağlar
        cv2.circle(img,points[idFrom],points[idFrom],3,(0,0,255),cv2.FILLED )
        cv2.circle(img,points[idFrom],points[idTo], 3,(0,0,255), cv2.FILLED)

cv2.imshow("Pose Estimation",img)
cv2.waitKey(0)

"""
import os
import requests as req
import cv2
import numpy as np

# İndirme URL'leri
image_url = "https://raw.githubusercontent.com/quanhua92/human-pose-estimation-opencv/master/image.jpg"
model_url = 'https://raw.githubusercontent.com/quanhua92/human-pose-estimation-opencv/master/graph_opt.pb'

# Görüntü dosyasını indir
if not os.path.exists('image.jpg'):
    img_data = req.get(image_url).content
    with open('image.jpg', 'wb') as fd:
        fd.write(img_data)

# Model dosyasını indir
if not os.path.exists('graph_opt.pb'):
    model_data = req.get(model_url).content
    with open('graph_opt.pb', 'wb') as fd:
        fd.write(model_data)

# Vücut parçaları ve bağlantılar
BODY_PARTS = {
    "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
    "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
    "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
    "LEye": 15, "REar": 16, "LEar": 17, "Background": 18
}

POSE_PAIRS = [
    ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
    ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
    ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
    ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
    ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]
]

# Modeli yükle
model = cv2.dnn.readNetFromTensorflow("graph_opt.pb")

# Görüntüyü yükle ve yeniden boyutlandır
img = cv2.imread("image.jpg")
img_new = cv2.resize(img, (900, 900))

# Görüntüyü göster (yeniden boyutlandırılmış)
cv2.imshow("New Image", img_new)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print(img_new.shape)

# Blob oluştur
blob = cv2.dnn.blobFromImage(img_new, 1.0, (img_new.shape[1], img_new.shape[0]), (127.5, 127.5, 127.5), swapRB=True, crop=False)
print(blob.shape)

# Blob'u modele input olarak ver
model.setInput(blob)
detect = model.forward()
print(detect.shape)

# Sadece gerekli olan ilk 19 kanalını kullan
detect = detect[:, :19, :, :]
print(detect.shape)

points = []

# Her bir vücut parçası için
for i in range(len(BODY_PARTS)):
    heatMap = detect[0, i, :, :]
    _, conf, _, maxLoc = cv2.minMaxLoc(heatMap)
    x = int((maxLoc[0] * img_new.shape[1]) / detect.shape[3])
    y = int((maxLoc[1] * img_new.shape[0]) / detect.shape[2])
    points.append((x, y) if conf > 0.25 else None)

print(f"points: {points}")

# Vücut parçalarını birleştiren çizgileri çiz
for pair in POSE_PAIRS:
    partFrom = pair[0]
    partTo = pair[1]

    idFrom = BODY_PARTS[partFrom]
    idTo = BODY_PARTS[partTo]

    if points[idFrom] and points[idTo]:
        cv2.line(img_new, points[idFrom], points[idTo], (0, 255, 0), 3)
        cv2.circle(img_new, points[idFrom], 3, (0, 0, 255), cv2.FILLED)
        cv2.circle(img_new, points[idTo], 3, (0, 0, 255), cv2.FILLED)

# Görüntüyü göster (pose tahmini ile)
cv2.imshow("Pose Estimation", img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
