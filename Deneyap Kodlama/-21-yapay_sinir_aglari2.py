import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.layers import Dense, Input, Dropout #Dense gizli katmanıdır. #
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Model
from keras.callbacks import EarlyStopping

df = pd.read_csv("INTELLIGENT IRRIGATION SYSTEM.csv")

print(df.head())

x=df.iloc[:,:2]
y=df.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)

#Keras
model=Sequential() #model taslağı oluşturur
model.add(Dense(200,input_dim=2,activation='relu')) #Giriş katman-input değeri- (nöron sayısı ,giren katman sayısı, aktivasyon fonksiyonu)
model.add(Dense(200,activation='relu')) #Gizli katman (nöron sayısı ,aktivasyon fonksiyonu)
model.add(Dense(200,activation='relu'))#Gizli katman (nöron sayısı ,aktivasyon fonksiyonu)
model.add(Dense(200,activation='relu'))#Gizli katman (nöron sayısı ,aktivasyon fonksiyonu)
model.add(Dense(200,activation='relu'))#Gizli katman (nöron sayısı ,aktivasyon fonksiyonu)
model.add(Dense(200,activation='relu'))#Gizli katman (nöron sayısı ,aktivasyon fonksiyonu)
model.add(Dense(1,activation='sigmoid'))#Çıkış katman (nöron sayısı ,aktivasyon fonksiyonu) #sigmoid = 0 ve 1 arasında değer verir
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy']) #(kayp oranı,en verimli hale getiren optimizer, doğruluk oranı )
model.summary() #özet


model.fit(x_train,y_train,epochs=2,batch_size=5,verbose=True)
pred=model.predict(x_test)
print(pred)
pred= (pred>0.5).flatten()
print(f"Doğruluk oranı: {metrics.accuracy_score(y_test,pred)}")

from sklearn.metrics import  confusion_matrix,ConfusionMatrixDisplay
import seaborn as sns
# Confusion matrix oluştur ve görselleştir
cm=confusion_matrix(y_test,pred)
index=["Çalışmıyor","Çalışıyor"]
columns=["Çalışmıyor","Çalışıyor"]
cm_df = pd.DataFrame(cm,columns,index)
plt.figure(figsize=(10,6))
sns.heatmap(cm_df, annot=True,fmt="d")
plt.show()
