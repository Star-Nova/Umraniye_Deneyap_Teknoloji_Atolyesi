import torch
from torch import nn
from torch import optim
import numpy as  np
"""
data_set=np.loadtxt("diabetes_data.csv",delimiter=',',skiprows=1)
print(data_set)
x=data_set[:,0:8]
y=data_set[:,-1]
print(x.shape,y.shape)
x=torch.tensor(x,dtype=torch.float32)
y=torch.tensor(x,dtype=torch.float32).reshape(-1,1)
model=nn.Sequential(
    nn.Linear(8,16),
    nn.ReLU(),
    nn.Linear(16,10),
    nn.ReLU(),
    nn.Linear(10,1),
    nn.Sigmoid()
)

print(model)
optimizer=optim.Adam(model.parameters(),lr=0.001)
loss=nn.BCELoss()
batch_size=10
total_epochs=500
for e in range(total_epochs):
    for i in range(0,len(x),batch_size):
        x_batch=x[i:i+batch_size]
        y_batch=y[i:i+batch_size]
        print(x_batch.shape,y_batch.shape)

        y_pred=model(x_batch)
        print(y_pred.shape)

        loss_s= loss(y_pred,y_batch) 
        optimizer.zero_grad() #Modelimiz grandyenlerde hataları saklar. Eğer bunlar olmazsa sistem çalışmaz
        loss_s.backward()
        optimizer.step()

    print(f"epoch: {e},loss: {loss_s}")
"""
import torch
from torch import nn
from torch import optim
import numpy as np

# Veri setini yükle
data_set = np.loadtxt("diabetes_data.csv", delimiter=',', skiprows=1)

# Veri setini özellikler ve hedef değişken olarak ayır
x = data_set[:, 0:8]
y = data_set[:, -1]

# Torch tensorlarına dönüştür
x = torch.tensor(x, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)

# Modeli tanımla
model = nn.Sequential(
    nn.Linear(8, 16),
    nn.ReLU(),
    nn.Linear(16, 10),
    nn.ReLU(),
    nn.Linear(10, 1),
    nn.Sigmoid()
)

# Modelin mimarisini yazdır
print(model)

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

        epoch_loss += loss.item()

    # Epoch başına ortalama kaybı yazdır
    print(f"Epoch {epoch + 1}/{total_epochs}, Kayıp: {epoch_loss / len(x)}")
