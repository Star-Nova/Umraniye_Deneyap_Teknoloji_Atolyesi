import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

df=pd.read_csv("housing.csv")

print(df.columns)

plt.hist(df["housing_median_age"])
plt.show()

price=df["median_house_value"]
rooms=df["total_rooms"]

plt.plot(price,rooms,"r--")

plt.title("Oda fiyat karşılaştırması")
plt.xlabel("fiyat")
plt.ylabel("oda sayısı")

plt.show()


iris = load_iris()
feature_names =iris.feature_names  #sepal dış yaprak epal ise iç yaprak denir iris çiçeğinde
data= pd.DataFrame(iris.data)
data.columns=feature_names

plt.title
plt.subplot(2,2,1)
plt.plot(data.iloc[:,1])
plt.show()

#kullanılacak


import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))


iris = load_iris()
feature_names =iris.feature_names  #sepal dış yaprak epal ise iç yaprak denir iris çiçeğinde
data= pd.DataFrame(iris.data)
data.columns=feature_names


plt.subplot(2,2,1)
plt.title(feature_names[0])
plt.plot(data.index, data[feature_names[0]],color="purple")

plt.subplot(2,2,2)
plt.title(feature_names[1])
plt.plot(data.index, data[feature_names[1]],color="black")

plt.subplot(2,2,3)
plt.title(feature_names[2])
plt.plot(data.index, data[feature_names[2]],color="#caa118")


plt.subplot(2,2,4)
plt.title(feature_names[3])
plt.plot(data.index, data[feature_names[3]],color="#7F7FFF")


plt.show()
