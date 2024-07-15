import cv2

img=cv2.imread("images/minik kedi.jpg") #resim okumayı sağlar


img_new=cv2.resize(img,(1500,705))
cv2.imshow("new image",img_new)
cv2.waitKey(1000)
print(img_new.shape)

h,w,c=img_new.shape
print("Yükseklik:",h) #Yüksekliğini verir
print("Genişlik:",w) #Genişliğini verir
print("Kanal Sayısı:",c) #Rgb renk kanalı
#rect(resim,başlangıç x-y, bitiş x,y , renk,kalınlık (x= yükseklik y=genişlik)
cv2.rectangle(img_new,(680,400),(1020,100),(200,145,36),5)

#Çember çiziyoruz
cv2.circle(img_new,(100,100),20,(200,145,36),3)
cv2.circle(img_new,(150,400),50,(200,145,36),9)
cv2.circle(img_new,(150,400),50,(200,145,36),-1) #Çemberin içini doldurmak için -1 yazıyoruz.
cv2.circle(img_new,(1100,500),10,(200,145,36),-1) #En küçük çember
cv2.circle(img_new,(1200,100),60,(200,145,36),3)

#Çubuk çiziyoruz
cv2.line(img_new,(10,10),(40,40),(200,145,36),4)


#Değeri küçültürsek yukarı büyültürsek aşşağı gider

cv2.putText(img_new,"Mavis",(750,90),cv2.FONT_HERSHEY_PLAIN,
            5,(200,145,36),5)



cv2.imshow("Cat",img_new)
cv2.waitKey(0)
