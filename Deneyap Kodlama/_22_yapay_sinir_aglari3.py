import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.layers import Dense, Input, Dropout
from sklearn import metrics
from sklearn.metrics import accuracy_score
import seaborn as sns
from tensorflow.keras.models import Model

import matplotlib.pyplot as plt
import pandas as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.layers import Dense, Input, Dropout
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Model
from keras.callbacks import EarlyStopping
from sklearn.metrics import r2_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import seaborn as sns

# Veri setini yükle
data = load_breast_cancer()
x, y = load_breast_cancer(return_X_y=True, as_frame=True)

# Veriyi eğitim ve test setlerine böl
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Veriyi DataFrame olarak oluştur
df_x = pd.DataFrame(x)
df_y = pd.DataFrame(y)

# İlk birkaç satırı yazdır
print(df_x.head())
print(df_y.head())

# Modeli oluştur
model = Sequential()

# Katmanları ekle
model.add(Dense(150, input_dim=30, activation="relu"))  # Giriş katmanı
model.add(Dense(150, activation="relu"))  # Gizli katman
model.add(Dense(150, activation="relu"))  # Gizli katman
model.add(Dense(150, activation="relu"))  # Gizli katman
model.add(Dense(150, activation="relu"))  # Gizli katman
model.add(Dense(150, activation="relu"))  # Gizli katman
model.add(Dense(1, activation="sigmoid"))  # Çıkış katmanı

# Modeli derle
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Modelin özetini yazdır
model.summary()

# Modeli eğit
history = model.fit(x_train, y_train, epochs=100, batch_size=5, verbose=True)

# Test verisi ile tahmin yap
pred = model.predict(x_test)
pred = (pred > 0.5).flatten()  # Tahminleri 0 veya 1 yap (eşik değeri 0.5)

# Doğruluk oranını yazdır
print("Doğruluk oranı: ", accuracy_score(y_test, pred))

# Confusion matrix oluştur ve görselleştir
cm = confusion_matrix(y_test, pred)
index = ["çalışmıyor", "çalışıyor"]
columns = ["çalışmıyor", "çalışıyor"]
cm_df = pd.DataFrame(cm, index, columns)
plt.figure(figsize=(10, 7))
sns.heatmap(cm_df, annot=True, fmt="d")
plt.show()

# Eğitim geçmişini (accuracy ve loss) görselleştir
plt.plot(history.history["accuracy"])
plt.plot(history.history["loss"])
plt.title("Doğruluk")
plt.ylabel("Değer")
plt.xlabel("Epoch")
plt.legend(["train", "test"], loc="upper right")
plt.show()

"Kategorik verileri sayısal verilere çevrildiğini unutma"