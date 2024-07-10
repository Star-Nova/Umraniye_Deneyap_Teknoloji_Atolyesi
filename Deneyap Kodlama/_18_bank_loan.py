import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import CategoricalNB
import seaborn as sns
from sklearn import preprocessing

# Pandas ayarları
pd.set_option("display.expand_frame_repr", False)

# CSV dosyasını Pandas DataFrame'e yükleme
veri_orijinal = pd.read_csv("loan.csv")
veri = veri_orijinal.copy()  # Verileri kopyalama

# Veri seti sütunlarını ve ilk beş satırını yazdırma
print(veri.columns)
print(veri.head())

# NaN değerleri içeren satırları silme
veri = veri.dropna() # veri.dropna() boş hücreleri sil

# 'loan_amnt' sütununun benzersiz değerlerini yazdırma
print(veri["loan_amnt"].unique())

# LabelEncoder kullanarak kategorik sütunları sayısal değerlere dönüştürme
sayisalalstirma = preprocessing.LabelEncoder()
veri["term"] = sayisalalstirma.fit_transform(veri["term"])
veri["purpose"] = sayisalalstirma.fit_transform(veri["purpose"])
veri["addr_state"] = sayisalalstirma.fit_transform(veri["addr_state"])
veri["home_ownership"] = sayisalalstirma.fit_transform(veri["home_ownership"])
veri["verification_status"] = sayisalalstirma.fit_transform(veri["verification_status"])

# İlk 20 satırı yazdırma
print(veri.head(20))

# Giriş (X) ve çıkış (Y) verilerini belirleme
x = np.array(veri.drop(["verification_status"], axis=1))
y = np.array(veri["verification_status"])

# Eğitim ve test setlerine ayırma
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=145)

# Categorical Naive Bayes modeli oluşturma ve eğitme
model = CategoricalNB()
model.fit(x_train, y_train)

# Test seti üzerinde tahmin yapma
pred = model.predict(x_test)

# Doğruluk oranını hesaplama
acc = accuracy_score(y_test, pred)
print("Doğruluk Oranı:", acc)
