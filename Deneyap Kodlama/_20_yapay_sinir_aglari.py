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
from sklearn.metrics import r2_score

# veriyi yükleme
dataset = pd.read_excel("ENB2012_data.xlsx")
dataset = dataset.values

# giriş ve çıkış verilerini ayırma
x = dataset[:, :8]
y = dataset[:, 8:]

# veri setini eğitim ve test olarak ayırma
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# veriyi 0 - 1 arasında ölçeklendirme
sc = StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.fit_transform(x_test)
x_train_scaled = np.array(x_train_scaled)
x_test_scaled = np.array(x_test_scaled)
y_train = np.array(y_train)
y_test = np.array(y_test)
y_train = (y_train[:,0],y_train[:,1])

input_layer = Input(shape=(x_train_scaled.shape[1],), name="input_layer")
common_layer = Dense(units=128, activation="relu", name="first_dense")(input_layer) #nöron sayısı
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
              loss={"First_output_last_layer":"mse","Second_output_last_layer":"mse"}, #hata oranını ölçen matris
              metrics={"First_output_last_layer":tf.keras.metrics.RootMeanSquaredError(),
              "Second_output_last_layer":tf.keras.metrics.RootMeanSquaredError()})

#Bir hata oluşursa sistem yeni bir şey öğrenemiyorsa sistem kendini kapatır
earlyStopping_callback = EarlyStopping(monitor="val_loss",
                                     min_delta=0, #durdurulacak hata oranı
                                     patience=10, #Nöronlar arsındaki etkileşim eğer bu değere ulaşrsa durur
                                     verbose=1) #Sonuçları ekranda gösterir

history = model.fit( x = x_train_scaled ,
                     y = y_train ,
                     verbose = 1 , #yapılan eğitimin ekranda gözükmesini sağlar
                     epochs = 500, #kaç eğitim yapılacağını gösterir
                     batch_size = 10, #kaçar veri alınacağını gösterir
                     validation_split = 0.3, #eğitim sırasında doğrulama oranı
                     callbacks = earlyStopping_callback
                    )

y_pred = np.array(model.predict(x_test_scaled))
print(y_pred)

print("İlk çıkışın r2 değeri : ", r2_score(y_test[:,0],y_pred[0,:].flatten()))
print("İkinci çıkışın r2 değeri : ", r2_score(y_test[:,1],y_pred[1,:].flatten()))

plt.figure(figsize=[15,10])
plt.subplot(1,2,1)
plt.plot(history.history["First_output_last_layer_root_mean_squared_error"])
plt.plot(history.history["Second_output_last_layer_root_mean_squared_error"])
plt.title("model\'s İlk çıkış için RMSE kayıp değerleri")
plt.ylabel("RMSE")
plt.xlabel("epochs")
plt.legend(["train","test"],loc = "upper right")
plt.subplot(1,2,2)
plt.plot(history.history["Second_output_last_layer_root_mean_squared_error"])
plt.plot(history.history["val_Second_output_last_layer_root_mean_squared_error"])
plt.title("model\'s ikinci çıkış için RMSE kayıp değerleri")
plt.ylabel("RMSE")
plt.xlabel("epochs")
plt.legend(["train","test"],loc = "upper right")
plt.show()




