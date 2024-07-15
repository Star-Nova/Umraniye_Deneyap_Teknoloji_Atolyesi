import cv2  #opencv açmak için kütüphanedir

img=cv2.imread("images/minik maymun.jpg") #resim okumayı sağlar
cv2.imshow("First image",img) #Resmi ekranda göster
cv2.waitKey(1000) #Eğer 0 yazarsan senin yazmanı bekler eğer 1000 yazarsan ekranda 1 saniye bekler sonra kapanır


h,w,c=img.shape
print("Yükseklik:",h) #Yüksekliğini verir
print("Genişlik:",w) #Genişliğini verir
print("Kanal Sayısı:",c) #Rgb renk kanalı

img_new=cv2.resize(img,(900,900))
cv2.imshow("new image",img_new)
cv2.waitKey(1000)
print(img_new.shape)

(b, g, r)=img_new[150,150] #Buradaki tek bir pikxelin bgr(rgb) renk kodunu verir.
print("R= {},G= {},B= {}".format(r,g,b))

center=(w//2,h//2) #İkiye küsüratsız bölmeyi sağlamak için çift bölme (//) işlemi kullanılır.
x=cv2.getRotationMatrix2D(center,-60,1) #Center merkez demek #-60 saat yönünde 60  derece döndürür
rotation_img=cv2.warpAffine(img_new,x,(w,h)) #rotation_img döndürülmüş resim demek
cv2.imshow("Rotation",rotation_img)
cv2.waitKey(1000)

slice=img_new[100:250,200:350]  #Önce yükseklik sora genişlik alınır (y,x) #Bu yötem le görselden belli bir parça alırız.
cv2.imshow("Slice",slice)
cv2.waitKey(1000)
