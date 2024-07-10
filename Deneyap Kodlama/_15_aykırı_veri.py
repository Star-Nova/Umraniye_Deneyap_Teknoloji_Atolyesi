"""
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

diabet=load_diabetes()
df_diabet =pd.DataFrame(diabet.data)
df_diabet.columns= diabet.feature_names
print(df_diabet.columns)

plt.figure(figsize=(10,7))
plt.boxplot(df_diabet["bmi"])
plt.title("bmi") #bmi, Body Mass Index (Vücut Kitle İndeksi) anlamına gelir
plt.show()

####################################################################################################

from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

diabet=load_diabetes()
df_diabet=pd.DataFrame(diabet.data)

df_diabet.columns=diabet.feature_names

print(df_diabet)
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
plt.boxplot(df_diabet["bmi"])
plt.title("bmi") #bmi, Body Mass Index (Vücut Kitle İndeksi) anlamına gelir
plt.subplot(1,2,2)
plt.boxplot(df_diabet["age"])
plt.title("age")
plt.show()

def outliner_filtrele(df,column,threshold):
    plt.figure(figsize=(10,7))
    plt.subplot(1, 2, 1)
    plt.boxplot(df_diabet["bmi"])
    plt.title("Filtreleme öncesi")


    filtrelenmis_degerler=df[df[column]<=threshold]
    plt.subplot(1, 2, 2)
    plt.boxplot(filtrelenmis_degerler[column])
    plt.title("Filtreleme sonrası")
    plt.show()

    return filtrelenmis_degerler
outliner_filtrele(df_diabet,"bmi",0.1)


#############################################################################################


def yeniveriyenikarsilastirma (df,column,threshold):
    plt.figure(figsize=(10,7))
    plt.subplot(1,2,1)
    plt.boxplot(df_diabet["s4"])
    plt.title("Filtreleme öncesi s4")

    filtrelenmis_degerler = df[df[column] <= threshold]
    plt.subplot(1, 2, 2)
    plt.boxplot(filtrelenmis_degerler[column])
    plt.title("Filtreleme sonrası s4")
    plt.show()

    return filtrelenmis_degerler


yeniveriyenikarsilastirma(df_diabet, "s4",0.1)

#aykırı değereri temizlemek yerine sütunun ortalaması alınacak
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#aykırı değereri temizlemek yerine sütunun ortalaması alınacak
def sutun_ortalamasi_aykiri_degistir(df, column,threshold):
    # Sütunun ortalamasını hesapla
    ortalama = np.mean(df[column])
    print(ortalama)
    plt.figure(figsize=(10, 7))
    plt.subplot(1,2,1)
    plt.boxplot(df_diabet["bmi"])
    plt.title("Filtreleme öncesi ")
    df[df[column]> threshold] = ortalama #amaç veris setinden kayıp vermemektir
    plt.subplot(1, 2, 2)
    plt.boxplot(df_diabet[column])
    plt.title("Filtreleme sonrası ")
    plt.show()

# 'bmi' sütunundaki aykırı değerleri ortalama ile değiştir
sutun_ortalamasi_aykiri_degistir(df_diabet, "bmi", 0.1)

#######################################################################################

#HATA VAR YARIN DÜZELTİLECEK

from scipy import stats
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
z_degerleri=np.abs(stats.zscore(df_diabet["bmi"]))
print(z_degerleri)
threseshold_z_skor=2
df_diabet.iloc[]
df_diabet['zdegeri']=z_degerleri
print(df_diabet.head())
df_diabet.drop(df_diabet[df_diabet['zdegeri']<threseshold_z_skor])
print(df_diabet.shape,x.shape)
"""
from sklearn.datasets import load_diabetes
import  pandas as pd
import numpy as np
diabet=load_diabetes()
sutun_isimleri=diabet.feature_names
df_diabet=pd.DataFrame(diabet.data)
df_diabet.columns=sutun_isimleri
print("IQR Öncesi Shape:",df_diabet.shape)
#Tespit Aşaması
Q1=df_diabet["bmi"].quantile(0.25)
Q3=df_diabet["bmi"].quantile(0.75)
IQR=Q3-Q1
print("IQR:",IQR)
L=Q1-1.5*IQR
U=Q1+1.5*IQR
print("Lower: {0} ve Upper: {1}".format(L,U))

#Filtreleme aşaması
upper_dizisi=np.where(df_diabet['bmi']>=U)[0]
lower_dizisi=np.where(df_diabet['bmi']<=L)[0]
df_diabet.drop(index=upper_dizisi, inplace=True)
df_diabet.drop(index=lower_dizisi, inplace=True)
print("IQR Sonrası Shape",df_diabet.shape)