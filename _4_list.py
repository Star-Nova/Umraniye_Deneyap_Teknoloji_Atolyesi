#Çalışmıyor
harf4 = []
harf5 = []
harf6 = []
isimler=[]

while True\
        :
    isim = input("İsim gir:")
    isimler.append(isim)


    for i in isimler:
        if len(i) == 4:
            harf4.append(i)
            break
        elif len(i) == 5:
            harf5.append(i)
            break
        elif len(i) == 6:
            harf6.append(i)
            break
        else:
            print(f"{i} kelimesinin harf sayısı bu listelerden birine ait değildir")
            break

print("4 Harfli İsimler:", harf4)
print("5 Harfli İsimler:", harf5)
print("6 Harfli İsimler:", harf6)
print("4 Harfli İsimler:", harf4)
print("5 Harfli İsimler:", harf5)
print("6 Harfli İsimler:", harf6)
