import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.layers import Dense, Input, Dropout
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Model
from keras.callbacks import EarlyStopping

# veriyi yükleme
dataset = pd.read_excel("ENB2012_data.xlsx")
dataset = dataset.values
print(dataset.shape)

# giriş ve çıkış verilerini ayırma
x = dataset[:, :8]
y = dataset[:, 8:]

# veri setini eğitim ve test olarak ayırma
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

print("\nX_train shape:", x_train.shape)
print("X_test shape:", x_test.shape)
print("Y_train shape:", y_train.shape)
print("Y_test shape:", y_test.shape)

# veriyi 0 - 1 arasında ölçeklendirme
sc = StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.fit_transform(x_test)
x_train_scaled = np.array(x_train_scaled)
x_test_scaled = np.array(x_test_scaled)
y_train = np.array(y_train)
y_test = np.array(y_test)
print(y_train)
y_train = (y_train[:,0],y_train[:,1])
print(y_train)
print(x_test_scaled)
print(x_train_scaled)

input_layer = Input(shape=(x_train_scaled.shape[1],), name="input_layer")
common_layer = Dense(units=128, activation="relu", name="first_dense")(input_layer)
common_layer = Dropout(0.3)(common_layer)

common_layer2 = Dense(units=128,activation="relu",name="second_dense")(common_layer)
common_layer2 = Dropout(0.3)(common_layer2)
first_output = Dense(units=1,name="First_output_last_layer")(common_layer2)

second_common_layer = Dense(units=64,activation="relu",name="second_layer_first_dense")(common_layer2)
second_common_layer = Dropout(0.3)(second_common_layer)
second_output = Dense(units=1,name="Second_output_last_layer")(second_common_layer)
model=Model(inputs=input_layer,outputs=[first_output,second_output])
print(model.summary())

optimizer=tf.keras.optimizers.SGD(learning_rate=0.00001)
model.compile(optimizer=optimizer,
              loss={"First_output_last_layer":"mse","Second_output_last_layer":"mse"},
              metrics={"First_output_last_layer":tf.keras.metrics.RootMeanSquaredError(),
              "Second_output_last_layer":tf.keras.metrics.RootMeanSquaredError()})
#Bir hata oluşursa sistem yeni bir şey öğrenemiyorsa sistem kendini kapatır
earlyStopping_callback=EarlyStopping(monitor="val_loss",
                                     min_delta=0,
                                     patience=10, #Nöronlar arsındaki etkileşim eğer bu değere ulaşrsa durur
                                     verbose=1) #Sonuçları ekranda gösterir



