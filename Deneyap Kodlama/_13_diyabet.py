from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
diyabet = load_diabetes(as_frame=True)
x = diyabet.data
y = diyabet.target
print(diyabet.feature_names)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5)
model = LogisticRegression()
model.fit(x_train,y_train) #Verileri eğitir
y_pred = model.predict(x_test)
acc = metrics.accuracy_score(y_test,y_pred) # Doğruluk skorunu hesaplar ve yazdır
print("doğruluk değeri (Accuracy) : ", acc)

