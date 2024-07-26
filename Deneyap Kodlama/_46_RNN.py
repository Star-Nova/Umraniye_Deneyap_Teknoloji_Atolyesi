import numpy as np
import os
import librosa
import fnmatch

data_path = "Heartbeat_Sound"
unlabel_data = os.path.join(data_path, "unlabel")
normal_data = os.path.join(data_path, "normal")
murmur_data = os.path.join(data_path, "murmur")
extrastole_data = os.path.join(data_path, "extrastole")


# Function to load and process sound files
def load_data(data_path, file_pattern, duration=10, sr=22050):
    input_length = sr * duration
    data = []
    labels = []

    # Get list of files that match the pattern
    file_names = fnmatch.filter(os.listdir(data_path), file_pattern)

    for file_name in file_names:
        try:
            sound_file = os.path.join(data_path, file_name)
            #print("Reading file:", sound_file)

            # Load audio file
            x, sr = librosa.load(sound_file, sr=sr, duration=duration)

            # Adjust length if necessary
            dur = librosa.get_duration(y=x, sr=sr)
            if round(dur) < duration:
                #print("Fixing length:", file_name)
                x = librosa.util.fix_length(x, size=input_length)

            # Compute MFCC features
            mfcc = np.mean(librosa.feature.mfcc(y=x, sr=sr, n_mfcc=25).T, axis=0)

            # Append data and corresponding label
            data.append(mfcc)
            labels.append(data_path.split('/')[-1])  # Assuming labels based on folder name

        except Exception as e:
            print("Error processing", file_name, ":", str(e))

    return data, labels


# Load data for each category
normal_sounds, normal_labels = load_data(normal_data, "normal*.wav")
murmur_sounds, murmur_labels = load_data(murmur_data, "murmur*.wav")
extrastole_sounds, extrastole_labels = load_data(extrastole_data, "extrastole*.wav")
unlabel_sounds, unlabel_labels = load_data(unlabel_data, "Bunlabel*.wav")

# Concatenate data and labels
x_data = np.concatenate((normal_sounds, murmur_sounds, extrastole_sounds))
y_data = np.concatenate((normal_labels, murmur_labels, extrastole_labels))

# Print shapes for verification
print("Shape of x_data:", x_data.shape)
print("Length of y_data:", len(y_data))
print("Unlabel data labels:", unlabel_labels)  # This will print the labels for unlabelled data

test_x = unlabel_sounds
test_y = unlabel_labels

import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, LSTM, Bidirectional, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.8,random_state=42,shuffle=True)
x_train,x_val,y_train,y_val = train_test_split(x_train,y_train,test_size=0.8,random_state=42,shuffle=True)


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_test =  le.fit_transform(y_test)
y_val =  le.fit_transform(y_val)
test_y =  le.fit_transform(test_y)

model = Sequential()
model.add(Bidirectional(LSTM(128,dropout=0.05,recurrent_dropout=0.20,
                             return_sequences=True),input_shape=(25,1)))
model.add(Dense(128,activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(128,activation="relu"))
model.add(Dense(128,activation="relu"))
model.add(Dense(128,activation="relu"))
model.add(Dense(128,activation="relu"))
model.add(Flatten())
model.add(Dense(3,activation="softmax"))
model.compile(loss="categorical_crossentropy",optimizer=Adam(1e-4),metrics=["acc"])
model.summary()
print(x_train.shape,y_train.shape)
history = model.fit(x_train,y_train, batch_size=3, epochs=20, validation_data=(x_val,y_val))
y_pred = model.predict(x_test,batch_size=5)
acc = model.evaluate(x_test,y_test)
print("Model DoÄŸruluk oranÄ±: ", acc)

