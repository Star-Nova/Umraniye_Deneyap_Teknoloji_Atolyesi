import cv2
img=cv2.imread("images/dog.jpg")

#https://albumentations.ai/ cv2deki malipülasyondaki yapacağımız alternatif

#istediğimiz boyutkara göre resmi yeniden düzenliyoruz. :D
img_new=cv2.resize(img,(1500,705))
cv2.imshow("new image",img_new)
cv2.waitKey(1000)
print(img_new.shape)

blur=cv2.GaussianBlur(img_new,(11,11),10) #bulanıklaştırma #SigmaX ne kadar bulur yapacağımızı söyler

grey=cv2.cvtColor(img_new,cv2.COLOR_BGR2GRAY) #Renkliden gri tonlamaya çevirir

edge=cv2.Canny(img_new,30,150)  #resimdeki nesnelerin hatlarını çizgi ile belli eder.

#Resmi gri tonlamadaki belirtilen eşik değerine göre siyah-beyaza çevirir.
t=cv2.threshold(grey,200,255,cv2.THRESH_BINARY)[1]
print(t)

cv2.imshow("Alaska Dog",t)
cv2.waitKey()