import cv2
"""
img=cv2.imread("images/friends.jpg")
#indirdiğimiz makine öğrenimini yükler
ml=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
print(ml)
#resmi gri tonlamaya çevirme
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#yüzlerin tespiti
faces=ml.detectMultiScale(gray)
print(faces)

#Tespit edilen yüzlerin çerçevelenmesi
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(25,212,36),3)

cv2.imshow("Face Detect",img)
cv2.waitKey(1000)#Ekranda ne kadar kalacağını ayarlarız

"""
import cv2

# Görüntüyü yükle
img = cv2.imread('/mnt/data/friends.jpg')

# Haar Cascade sınıflandırıcıyı yükle
ml = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if ml.empty():
    print("Haar Cascade yüklenemedi.")
else:
    print("Haar Cascade başarıyla yüklendi.")

# Görüntüyü gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Yüzlerin tespiti
faces = ml.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
print(faces)

# Tespit edilen yüzlerin çerçevelenmesi
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 212, 36), 3)

# Görüntüyü göster
cv2.imshow('Face Detect', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
