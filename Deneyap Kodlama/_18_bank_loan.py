import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.naive_bayes import CategoricalNB
import seaborn as sns
from sklearn import preprocessing

pd.set_option=("display.expand_frame_repr",False)
veri_orijinal=pd.read_csv("loan.csv")
veri=veri_orijinal.copy()
print(veri.columns)
print(veri.head())
veri= veri.dropna() # veri.dropna() boş hücreleri sil
print(veri["loan_amnt"].unique())
sayisalalstirma=preprocessing.LabelEncoder()
veri["term"]=sayisalalstirma.fit_transform(veri["term"])
veri["purpose"]=sayisalalstirma.fit_transform(veri["purpose"])
veri["addr_state"]=sayisalalstirma.fit_transform(veri["addr_state"])
veri["home_ownership"]=sayisalalstirma.fit_transform(veri["home_ownership"])
veri["verification_status"]=sayisalalstirma.fit_transform(veri["verification_status"])
print(veri.head(20))
x=np.array(veri.drop(["verification_status"],axis=1))
y=np.array(veri["verification_status"])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=145)
model=CategoricalNB()
model.fit(x_train,y_train)
pred=model.predict(x_test)
acc=accuracy_score(y_test,pred)
print("Doğruluk oranı:",acc)