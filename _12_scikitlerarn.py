import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import metrics

# Iris veri setini yükle
iris = load_iris()

# Veri ve etiketleri ayır
x = iris.data  # Özellikler
y = iris.target  # Sınıflar

# Veriyi eğitim ve test setlerine ayır
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)  # test_size=0.2 veri setinin %20'si test için kullanılacak

# Eğitim ve test veri setlerinin boyutlarını yazdır
print("x_train shape:", x_train.shape)
print("y_train shape:", y_train.shape)
print("x_test shape:", x_test.shape)
print("y_test shape:", y_test.shape)

# KNN sınıflandırıcı oluştur ve eğitim verisiyle eğit
knn = KNeighborsClassifier(n_neighbors=7, metric="euclidean")  # k en yakın komşu sayısını 7 ve uzaklık ölçütü olarak Öklidyen mesafeyi kullan
knn.fit(x_train, y_train)

# Test verisi ile tahmin yap
y_pred = knn.predict(x_test)

# Doğruluk skorunu hesapla ve yazdır
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Doğruluk değeri (Accuracy):", accuracy)
print(metrics.confusion_matrix(y_test,y_pred))

"""
1-Veri seti almak
2-Veriyi eğitim ve test olarak ayırmak
3-Yapay Zeka Modeli seçmek
4-Modeli eğitmek(fit,predict)
5-Doğruluğunu test etmek

"""
plt.figure(figsize=(10,7))
plt.plot(y_test,y_pred)
plt.scatter(y_test,y_pred)
plt.show()