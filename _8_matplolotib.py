#Grafik oluşturma
import matplotlib.pyplot as plt

"""
x= [11,12,13,14,15,16,17,18,19,20]
y= [1,2,3,4,5,6,7,8,9,10]

plt.plot(x,y)
plt.title("Çizgi Grafigi") #sütunun adı
plt.legend("Araba") #sutunun açıklaması
plt.show() #çizimi göster

plt.bar(x,y) #Çubuk grafiği
plt.title("Çubuk Grafigi") #sütunun adı
plt.legend("Araba") #sutunun açıklaması
plt.show() #çizimi göster

import random as rnd
import matplotlib.pyplot as plt  # matplotlib kütüphanesini içe aktarıyoruz

# Rastgele sayılar oluşturuyoruz
yeni_veri = [rnd.randint(1, 100) for _ in range(20)] #Not rnd random metodunun kısaltmasıdır

# Histogram oluşturuyoruz
plt.hist(yeni_veri)  # Dağılım grafiğini çizdirir
plt.title("Histogram")  # Grafik başlığı
plt.show()  # Grafiği gösterir


plt.scatter(x,y) #nokta  grafiği
plt.title("Nokta Grafigi") #sütunun adı
plt.legend("Araba") #sutunun açıklaması
plt.show() #çizimi göster

veri=[10,20,50,30] #pasta grafiği
etiketler=["Java","python","C++","Scratch"]
plt.figure(figsize=(10,8))
plt.pie(veri,labels=etiketler)
plt.show()

import matplotlib.pyplot as plt

# Verileri güncelliyoruz
kodlama_suresi = [5, 3, 4, 10, 13, 12, 0]  # 7. gün için 0 ekliyoruz
dinlenme_suresi = [10, 12, 9, 11, 8, 6, 6]
gunler = [1, 2, 3, 4, 5, 6, 7]

# Grafik çizimi
plt.stackplot(gunler, kodlama_suresi, dinlenme_suresi, colors=["blue", "orange"])
plt.xlabel("Günler")
plt.ylabel("Saat")
plt.legend(["Kodlama Süresi", "Dinlenme Süresi"])
plt.title("Kodlama ve Dinlenme Süresi")
plt.show()
"""

import matplotlib.pyplot as plt

# İlk subplot
x = [70, 88, 92, 99]
y = [43, 80, 46, 100]
plt.subplot(2, 1, 1)  # 2 satır, 1 sütun, 1. subplot
plt.plot(x, y)

# İkinci subplot
a = [7, 86, 90, 10]
b = [4, 80, 48, 101]
plt.subplot(2, 1, 2)  # 2 satır, 1 sütun, 2. subplot
plt.plot(a, b)
plt.plot(a, b, "--", color="green")  # Yeşil kesik çizgiyle ikinci grafiği çiz

# Grafik gösterimi
plt.show()



fss=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
ardisik=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
plt.scatter(1, 1, 1)  # 2 satır, 1 sütun, 2. subplot

plt.plot(fss, ardisik)
plt.stackplot(fss, ardisik, colors=["orange", "orange"])
plt.xlabel("Ardışık Sayılar")
plt.ylabel("Fibonacci Sayı Sistemi")
plt.show()

#Fibonacci sayı sistemi
#1den 15 kadar
#İki farklı grafikte ekrana sun
