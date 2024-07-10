from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

veri = fetch_california_housing()
sutun_isimleri = veri.feature_names
df_veri = pd.DataFrame(veri.data)
df_veri.columns = sutun_isimleri
print(df_veri.columns)

figsize = plt.figure(figsize=(10,7))
plt.subplot(1,3,1)
plt.boxplot(df_veri["Population"])
plt.title("orijinal veri")

print("Orijinal data boyutu : ",df_veri.shape)
zdegeri = np.abs(stats.zscore(df_veri["Population"]))

print("Z skoru : ",zdegeri)
threshold_z = 2

aykiri = np.where(zdegeri > threshold_z)[0]
filtreli_tablo = df_veri.drop(aykiri)
print("Z skoru sonrası: ",filtreli_tablo.shape)

plt.subplot(1,3,2)
plt.boxplot(filtreli_tablo["Population"])
plt.title("Zskor veri")

q1 = df_veri["Population"].quantile(0.25)
q3 = df_veri["Population"].quantile(0.75)

iqr = q3-q1

print("IQR",iqr)

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print("en yüksek ve en düşük : " , upper,lower)

yd = np.where(df_veri["Population"] >= upper)[0]
dd = np.where(df_veri["Population"] <= lower)[0]

df_veri.drop(index = yd,inplace=True)
df_veri.drop(index = dd,inplace=True)

print("IQR sonrası shape",df_veri.shape)

plt.subplot(1,3,3)
plt.boxplot(df_veri["Population"])
plt.title("IQR veri")
plt.show()







