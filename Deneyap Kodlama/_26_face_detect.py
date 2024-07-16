import cv2

img=cv2.imread("images/friends.jpg")
#indirdiğimiz makine öğrenimini yükler
ml=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#resmi gri tonlamaya çevirme
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#yüzlerin tespiti
faces=ml.detectMultiScale(gray)
print(faces)

#Tespit edilen yüzlerin çerçevelenmesi
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(25,212,36),3)

cv2.imshow("Face Detect",img)
cv2.waitKey(0)#Ekranda ne kadar kalacağını ayarlarız