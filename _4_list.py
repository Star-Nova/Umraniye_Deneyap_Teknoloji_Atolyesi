# İsimler için listeler
harf4 = []
harf5 = []
harf6 = []

while True:
    isim = input("İsim gir (Çıkmak için 'q' tuşuna basın): ")
    
    if isim.lower() == 'q':  # Çıkmak için 'q' girilirse döngüden çık
        break
    
    if len(isim) == 4:
        harf4.append(isim)
    elif len(isim) == 5:
        harf5.append(isim)
    elif len(isim) == 6:
        harf6.append(isim)
    else:
        print(f"'{isim}' kelimesinin harf sayısı bu listelerden birine ait değildir")

# Sonuçları yazdır
print("4 Harfli İsimler:", harf4)
print("5 Harfli İsimler:", harf5)
print("6 Harfli İsimler:", harf6)
