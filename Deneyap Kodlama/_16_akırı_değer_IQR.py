# Gerekli kütüphanelerin yüklenmesi
from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# California Housing veri setinin yüklenmesi
veri = fetch_california_housing()

# Veri setindeki sütun isimlerinin alınması
sutun_isimleri = veri.feature_names

# Veri setinin DataFrame'e dönüştürülmesi
df_veri = pd.DataFrame(veri.data)

# DataFrame sütun isimlerinin ayarlanması
df_veri.columns = sutun_isimleri
print(df_veri.columns)

# Grafik boyutlarının ayarlanması
figsize = plt.figure(figsize=(10, 7))  # Dosyanın boyutunu ayarlamamızı sağlar

# Orijinal veri için Boxplot oluşturulması
plt.subplot(1, 3, 1)
plt.boxplot(df_veri["Population"])
plt.title("Orijinal Veri")

# Orijinal veri setinin boyutunun yazdırılması
print("Orijinal data boyutu: ", df_veri.shape)  # Boyutunu verir

# 'Population' sütunu için Z-skorlarının hesaplanması
zdegeri = np.abs(stats.zscore(df_veri["Population"]))  # İstatistiksel analiz ve hesaplamalar yapmak için stats kullanılır

# Z-skorlarının yazdırılması
print("Z skoru: ", zdegeri)

# Z-skoru için eşik değeri belirlenmesi
threshold_z = 2

# Eşik değerini aşan aykırı değerlerin tespiti
aykiri = np.where(zdegeri > threshold_z)[0]

# Aykırı değerlerin veri setinden çıkarılması
filtreli_tablo = df_veri.drop(aykiri)
print("Z skoru sonrası: ", filtreli_tablo.shape)

# Z-skoru filtreli veri için Boxplot oluşturulması
plt.subplot(1, 3, 2)
plt.boxplot(filtreli_tablo["Population"])
plt.title("Z-skor Veri")

# İlk çeyrek (Q1) ve üçüncü çeyrek (Q3) hesaplanması
q1 = df_veri["Population"].quantile(0.25)
q3 = df_veri["Population"].quantile(0.75)

# Çeyrekler arası açıklığın (IQR) hesaplanması
iqr = q3 - q1
print("IQR: ", iqr)

# Alt ve üst sınırların belirlenmesi (1.5 * IQR kuralı)
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print("En yüksek ve en düşük: ", upper, lower)

# Alt ve üst sınırları aşan aykırı değerlerin tespiti
yd = np.where(df_veri["Population"] >= upper)[0]
dd = np.where(df_veri["Population"] <= lower)[0]

# Aykırı değerlerin veri setinden çıkarılması
df_veri.drop(index=yd, inplace=True)
df_veri.drop(index=dd, inplace=True)

# IQR sonrası veri setinin boyutunun yazdırılması
print("IQR sonrası shape: ", df_veri.shape)

# IQR filtreli veri için Boxplot oluşturulması
plt.subplot(1, 3, 3)
plt.boxplot(df_veri["Population"])
plt.title("IQR Veri")

# Grafiklerin gösterilmesi
plt.show()
