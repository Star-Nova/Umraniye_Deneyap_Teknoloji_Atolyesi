import pandas as pd
import numpy as np
import torch
from torch import nn
from torch import optim

# Veri setini oku
data_set = pd.read_csv("Debernardi et al 2020 data.csv")
print(data_set.columns)
print(data_set["diagnosis"].unique())
x=data_set.drop(columns=["sex","patient_cohort","sample_origin","diagnosis"])
y=data_set["diagnosis"]
print(x.shape)
print(y.shape)


x=x.to_numpy()

# Veri setini özellikler ve hedef değişken olarak ayır
x = data_set.iloc[:, 0:8].values
y = data_set.iloc[:, -1].values

# Torch tensorlarına dönüştür
x = torch.tensor(x, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)

# Modeli tanımla
model = nn.Sequential(
    nn.Linear(10, 16),
    nn.ReLU(),
    nn.Linear(16, 10),
    nn.ReLU(),
    nn.Linear(10, 3),
    nn.Softmax(dim=1) #0 ile 1 arasında değiştirir.
)

# Optimizatör ve kayıp fonksiyonunu tanımla
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.BCELoss() #BCELoss (binary_crossentropy)

# Eğitim parametreleri
batch_size = 10
total_epochs = 500

# Eğitim döngüsü
for epoch in range(total_epochs):
    epoch_loss = 0
    for i in range(0, len(x), batch_size):
        x_batch = x[i:i + batch_size]
        y_batch = y[i:i + batch_size]

        # İleri besleme
        y_pred = model(x_batch)

        # Kayıp hesapla
        loss = loss_fn(y_pred, y_batch)

        # Geri yayılım ve optimizasyon
        optimizer.zero_grad() #Modelimiz grandyenlerde hataları saklar. Eğer bunlar olmazsa sistem çalışmaz
        loss.backward() #Tahmin ettiğimiz değerler ile gerçek değerleri karışaltırır.
        optimizer.step()
