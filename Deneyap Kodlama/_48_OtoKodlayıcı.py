from keras import layers
from keras.datasets import mnist
from keras.models import Model
import numpy as np
import matplotlib.pyplot as plt

def preprocessing(array):
    array = array.astype("float32") / 255.0
    array = np.reshape(array, (len(array), 28, 28, 1))
    return array

def viewing(array1, array2):
    n = 20
    indices = np.random.randint(len(array1), size=n)
    images1 = array1[indices, :]
    images2 = array2[indices, :]

    plt.figure(figsize=(20, 4))
    for i, (image1, image2) in enumerate(zip(images1, images2)):
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(image1.reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(image2.reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()

def noise(array):
    noise_factor = 0.4
    noisy_array = array + noise_factor * np.random.normal(
        loc=0.0, scale=1.0, size=array.shape
    )
    return np.clip(noisy_array, 0.0, 1.0)

(train_data, _), (test_data, _) = mnist.load_data()

train_data = preprocessing(train_data)
test_data = preprocessing(test_data)

noisy_train_data = noise(train_data)
noisy_test_data = noise(test_data)

viewing(train_data, noisy_train_data)

input = layers.Input(shape=(28, 28, 1))

#Kodlayıcı (Encoder)
x = layers.Conv2D(32, (3, 3), activation="relu", padding="same")(input)
x = layers.MaxPooling2D((2, 2), padding="same")(x)
x = layers.Conv2D(32, (3, 3), activation="relu", padding="same")(x)
x = layers.MaxPooling2D((2, 2), padding="same")(x)

#Kod Çözücü (Decoder)
x = layers.Conv2DTranspose(32, (3, 3), strides=2, activation="relu", padding="same")(x)
x = layers.Conv2DTranspose(32, (3, 3), strides=2, activation="relu", padding="same")(x)
x = layers.Conv2D(1, (3, 3), activation="sigmoid", padding="same")(x)

autoencoder = Model(input, x)
autoencoder.compile(optimizer="adam", loss="binary_crossentropy")
autoencoder.summary()

#Orijinal veriyle eğitim
autoencoder.fit(
    x=train_data,
    y=train_data,
    epochs=10,
    batch_size=64,
    shuffle=True,
    validation_data=(test_data, test_data),)

predictions = autoencoder.predict(test_data)
viewing(test_data, predictions)

#Gürültülü veriyle eğitim
autoencoder.fit(
    x=noisy_train_data,
    y=train_data,
    epochs=10,
    batch_size=128,
    shuffle=True,
    validation_data=(noisy_test_data, test_data),
)

predicted = autoencoder.predict(noisy_test_data)
viewing(noisy_test_data, predicted)
