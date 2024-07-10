from PIL import Image
from glob import glob
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier as karar_agaci
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics

# Dosya yollarını tanımlama
covidli_path = "archive\\COVID\\*.png"
covidli_olmayan_path = "archive\\non-COVID\\*.png"
covidli = glob(covidli_path)
covidli_olmayan = glob(covidli_olmayan_path)

def veri_donusturme(dosyalar, sinif_adi):
    goruntu_sinifi = []
    for dosya in dosyalar:
        goruntu = Image.open(dosya).convert("L")  # gri tonlama
        goruntu_boyutlandir = goruntu.resize((28, 28))  # resize((28,28)) görüntü boyutunu ayarlarız
        goruntu_donusturme = np.array(goruntu_boyutlandir).flatten()  # matrisi tek boyutlu hale getirir
        veriler = np.append(goruntu_donusturme, [sinif_adi])
        goruntu_sinifi.append(veriler)
    return goruntu_sinifi

# Verileri işleme
covidli_veri = veri_donusturme(covidli, 0)
covidsiz_veri = veri_donusturme(covidli_olmayan, 1)

# Verileri DataFrame'e dönüştürme
covidli_veri_df = pd.DataFrame(covidli_veri)
covidsiz_veri_df = pd.DataFrame(covidsiz_veri)
tum_veri = pd.concat([covidli_veri_df, covidsiz_veri_df])

# Giriş ve çıkış verilerini ayırma
giris = np.array(tum_veri.iloc[:, :-1])
cikis = np.array(tum_veri.iloc[:, -1])

# Eğitim ve test verilerini ayırma
giris_train, giris_test, cikis_train, cikis_test = train_test_split(giris, cikis, test_size=0.2)

# Modeli oluşturma ve eğitme
model = karar_agaci()
clf = model.fit(giris_train, cikis_train)

# Tahmin yapma
pred = clf.predict(giris_test)

# Sonuçları yazdırma
print("Tahminler:", pred[:10])
print("Gerçekler:", cikis_test[:10])
acc = accuracy_score(cikis_test, pred)
print("Doğruluk oranı:", acc)

import matplotlib.pyplot as cizim

ypo,dpo,threshold=metrics.roc_curve(cikis_test,pred)
roc_auc=metrics.auc(ypo,dpo)
cizim.title("Roc eğrisi")
cizim.plot(ypo,dpo,'b',label='AUC=%0.2f'%roc_auc)
cizim.legend(loc='lower right')
cizim.plot([0,1],[0,1],'r--')
cizim.xlim([0,1])
cizim.ylim([0,1])
cizim.ylabel("Doğru Pozitif Oranı")
cizim.xlabel("Yanlış Pozitif Oranı")
cizim.show()