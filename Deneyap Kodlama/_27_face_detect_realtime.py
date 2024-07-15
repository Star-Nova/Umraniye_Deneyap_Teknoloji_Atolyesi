import cv2

#indirdiğimiz makine öğrenimini yükler
ml=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#videoyu açmak
cap=cv2.VideoCapture(0) #0 varsayılan kamera

while True:
    _, frame = cap.read() #alt tire ( _ ) yerine istediğini yazabilirsin. #Kameradan anlık resimleri alır.
    #resmi griye çevirme
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #yüzleri bulma
    faces= ml.detectMultiScale(frame)
    #yüzleri çerçevelendirmek
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(12,255,99),4)

    cv2.imshow("Face Detect",frame)
    cv2.waitKey(0)#Ekranda ne kadar kalacağını ayarlarız