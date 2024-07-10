import numpy as np
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
veri_orjinal = pd.read_csv("car.csv",encoding="unicode_escape")
veri = veri_orjinal.copy()
print(veri.head())
print(veri["fiyat"].unique())
print(veri["onarim"].unique())
print(veri["bagaj boyutu"].unique())
print(veri["Guvenlik"].unique())
print(veri["satis "].unique())
sayisal = preprocessing.LabelEncoder() #Kategorik verileri sayısal ifadelere dönüştürür
print(veri["fiyat"].unique())
print(veri["onarim"].unique())
print(veri["bagaj boyutu"].unique())
print(veri["Guvenlik"].unique())
print(veri["satis "].unique())
veri["fiyat"] = sayisal.fit_transform(veri["fiyat"])
veri["onarim"] = sayisal.fit_transform(veri["onarim"])
veri["kapi sayisi"] = sayisal.fit_transform(veri["kapi sayisi"])
veri["kisi sayisi"] = sayisal.fit_transform(veri["kisi sayisi"])
veri["bagaj boyutu"] = sayisal.fit_transform(veri["bagaj boyutu"])
veri["Guvenlik"] = sayisal.fit_transform(veri["Guvenlik"])
veri["satis "] = sayisal.fit_transform(veri["satis "])
print(veri.head())
giris = np.array(veri.drop(["satis "],axis=1))
print(giris)
cikis = np.array(veri["satis "])

from sklearn.model_selection import train_test_split
giris_egitim,giris_test,cikis_egitim,cikis_test = train_test_split(giris,cikis,test_size=0.3,random_state=109)

from sklearn.naive_bayes import CategoricalNB
model = CategoricalNB()
model.fit(giris_egitim,cikis_egitim)
satis_tahmin = model.predict(giris_test)

from sklearn.metrics import confusion_matrix
import seaborn as sns
cm = confusion_matrix(cikis_test,satis_tahmin)
print(cm)
index =["zor",'normal', 'çok kolay', 'kolay']
columns =["zor",'normal', 'çok kolay', 'kolay']
cm_df = pd.DataFrame(cm,columns,index)

plt.figure(figsize=(10,7))
sns.heatmap(cm_df,annot=True,fmt="d")
plt.show()

from sklearn.metrics import accuracy_score
acc = accuracy_score(cikis_test,satis_tahmin)
print("Doğruluk Oranı:", acc)
