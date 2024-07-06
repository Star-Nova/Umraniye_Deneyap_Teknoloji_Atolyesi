import numpy as np

"""
# Tek boyutlu bir dizi oluşturma
dizi = np.array([10, 20, 30, 40])
print(f"Bu tek boyutlu bir dizi: {dizi}")

"""
# Çok boyutlu bir dizi (3x2 boyutunda)
dizi2 = np.array([[10, 20], [30, 40], [50, 60]])
print(f"Çok boyutlu (3x2) dizi:\n{dizi2}")

"""
# Listeyi numpy dizisine çevirme
liste = [1, 2, 3, 4, 5]
dizi3 = np.array(liste)
print("Liste:", liste)
print("Diziye çevrilmiş hali:", dizi3)

# Belirli aralıklarla tek boyutlu dizi oluşturma
dizi4 = np.arange(1, 20)
print("1'den 19'a kadar (aralıklar dahil değil):", dizi4)

# Belirli aralıklarla (step size ile) dizi oluşturma
dizi5 = np.arange(1, 10, 2)
print("1'den başlayarak 2'şer artışlarla:", dizi5)

# Tüm elemanları sıfır olan çok boyutlu bir dizi oluşturma
zeros = np.zeros([3, 3, 3])
print("3x3x3 boyutunda sıfırlardan oluşan dizi:\n", zeros)

# Tüm elemanları bir olan 2x2 bir dizi oluşturma
ones = np.ones([2, 2])
print("2x2 boyutunda birlerden oluşan dizi:\n", ones)

# Birim matris (identity matrix) oluşturma
eye = np.eye(6, 6)
print("6x6 birim matris:\n", eye)

# Eşit aralıklarla dizi oluşturma (1'den 10'a kadar 5 elemanlı)
linspace = np.linspace(1, 10, 5)
print("1 ile 10 arasında 5 eşit aralıkla elemanlar:", linspace)

# Rastgele değerlerle dizi oluşturma ve 10 ekleme
rst = np.random.rand(2, 2) + 10
print("Rastgele 2x2 dizi ve her elemana 10 eklenmiş hali:\n", rst)

# Normal dağılımdan rastgele 3 sayı içeren dizi oluşturma
rst_normal = np.random.rand(3)
print("Normal dağılımdan rastgele 3 sayı içeren dizi:", rst_normal)

# Rastgele tam sayılar içeren 2x2 bir dizi
rnd = np.random.randint(1, 10, [2, 2])
print("Rastgele tam sayılar içeren 2x2 dizi:\n", rnd)

# Dizi bilgileri
print("Satır ve sütun boyutu:", rnd.shape)
print("Boyut bilgisi (ndim):", rnd.ndim)
print("Her bir elemanın bellek boyutu (byte):", rnd.itemsize)

# Dizi işlemleri
a = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
b = np.array([9, 10, 11])

# Diziler arasında aritmetik işlemler
print("İki dizi toplamı:\n", np.add(a, b))
print("İki dizi farkı:\n", np.subtract(a, b))
print("İki dizi toplamı (a + b):\n", a + b)
print("Negatif dizi (b):\n", -b)
print("İki dizi çarpımı:\n", np.multiply(a, b))
print("Dizinin elemanları toplamı:", np.sum(a))
print("Dizideki maksimum ve minimum değer:", np.max(a), np.min(b))
print("Dizinin ortalama değeri:", np.mean(a))
print("Dizinin standart sapması:", np.std(a))

# Çok boyutlu bir dizi oluşturma
cok_boyutlu_dizi = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                             [[1, 2, 3, 4], [9, 10, 11, 12]]], dtype=np.int64)
print("Çok boyutlu dizi:\n", cok_boyutlu_dizi)
print("Dizinin belirli elemanına erişim (1,1,1):", cok_boyutlu_dizi[1, 1, 1])
print("Dizinin belirli elemanına erişim (0,1):", cok_boyutlu_dizi[0, 1])

# Rastgele değerler içeren 3x3x3 dizi
rnd_3d = np.random.randint(-10, 10, [3, 3, 3])
print("Rastgele 3x3x3 dizi:\n", rnd_3d)

# Dizideki belirli koşullara uygun elemanları filtreleme
print("Pozitif değerler:", rnd_3d[rnd_3d > 0])
print("Negatif değerler:", rnd_3d[rnd_3d < 0])
print("Çift sayılar:", rnd_3d[rnd_3d % 2 == 0])
print("Tek sayılar:", rnd_3d[rnd_3d % 2 != 0])

# Dizi bilgileri
print("Dizinin satır ve sütun bilgisi (shape):", rnd_3d.shape)
print("Dizinin transpoz (T) shape bilgisi:", rnd_3d.T.shape)  # Transpoz dizi boyutu
rnd_3d.resize(2, 2, 2)
print("Dizinin yeniden boyutlandırılmış hali (resize):", rnd_3d.shape)

"""