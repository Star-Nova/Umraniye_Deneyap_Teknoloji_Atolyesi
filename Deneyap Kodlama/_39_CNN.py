import tensorflow
import numpy as np
import keras.utils as image
import tensorflow.python.keras.models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import time

"""veriyi ayırma"""

train_datagen = ImageDataGenerator(
    rescale = 1./225, #bir resimdeki pikselleri 0 ile 1 arasına çekiyor.
    shear_range = 0.2, #görütüleri rastgele kesme dönüşümler ugular
    zoom_range = 0.2, #görüntülere rastgele yaklaştırmalar uygular
    horizontal_flip = True #görüntüyü yatayda çevir
)

train_dataset = train_datagen.flow_from_directory(
    "dataset/train", #yol
    target_size = (64,64), #resimlerin boyutu
    batch_size = 32, #tek seferde işlencek resim miktarı
    class_mode = "binary", #ikili sınıflandırma
)


test_datagen = ImageDataGenerator(rescale = 1./225)

test_dataset = test_datagen.flow_from_directory(
    "dataset/test",
    target_size = (64, 64),
    batch_size = 32,
    class_mode = "binary",
)

#yapay zeka modelini ve katmanları oluşturma

model = tensorflow.keras.models.Sequential()
model.add(tensorflow.keras.layers.Conv2D(
    filters = 32, #32 filtresi var her filtre görüntüde farklı özelliği öğrenir
    kernel_size = 3, #filtrelin boyutu
    activation = "relu",
    input_shape = [64,64,3] #girdi resmin boyutları
))

model.add(tensorflow.keras.layers.MaxPool2D(
    pool_size = 2, #havuzlama pencere boyutu
    strides = 2, #havuzlama penceresinin kayma adımı
))

model.add(tensorflow.keras.layers.Conv2D(
    filters = 32,
    kernel_size = 3,
    activation = "relu",
))

model.add(tensorflow.keras.layers.MaxPool2D(
    pool_size = 2,
    strides = 2,
))

model.add(tensorflow.keras.layers.Conv2D(
    filters = 32,
    kernel_size = 3,
    activation = "relu",
))

model.add(tensorflow.keras.layers.MaxPool2D(
    pool_size = 2,
    strides = 2,
))

model.add(tensorflow.keras.layers.Conv2D(
    filters = 32,
    kernel_size = 3,
    activation = "relu",
))

model.add(tensorflow.keras.layers.MaxPool2D(
    pool_size = 2,
    strides = 2,
))

model.add(tensorflow.keras.layers.Flatten()) #resmi tek boyutlu yapar

model.add(tensorflow.keras.layers.Dense(
    units=128,
    activation="relu"
))

model.add(tensorflow.keras.layers.Dense(
    units=1,
    activation="sigmoid"
))

model.compile(optimizer = "Adam",loss = "binary_crossentropy",metrics = ["accuracy"])
print(model.summary())

model.fit(x = train_dataset,validation_data = test_dataset,epochs = 100 )
loss,acc = model.evaluate(test_dataset)
print("Eğitimin sonundaki doğruluk oranı : ",acc)
print("Eğitimin sonundaki loss : ",loss)

test_data = image.load_img("tumor-dataset/deneme/Y12.jpg",target_size = (64,64)) #resmi yükler
test_data = image.img_to_array(test_data) #array e çevirir
test_data = np.expand_dims(test_data,axis=0) #yeni eksen ekler ve dizi boyutu değişir
output = model.predict(test_data)
train_dataset.class_indices #trainin içindeki sınıf indexlerini verir

print(train_dataset.class_indices)

if output[0][0] == 1 :
    print("Sonuç = Tümör tespit edildi")
else:
    print("Sonuç = Tümör tespit edilemedi")

model.save("model_cnn.h5")
model.save("model_cnn"+time.strftime("%d.%m.%Y -- %H.%M.%S")+".h5")

