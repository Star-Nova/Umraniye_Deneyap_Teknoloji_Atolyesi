import pandas
import pandas as pd
pd.set_option("display.expand_frame_repr", False) #bütün sütunları tam görebilmek için
df=pd.read_csv("housing.csv")  #Bir csv dosyasını okuma
"""
int(df.head(10)) #tablonun ilk 10 satırnı görürüz
print(df.tail(10)) #tablonun son 10 satırnı görürüz
print(df.info) #tablo hakkında özet bilgi verir
print(df.columns) #tablodaki sütunları bize yazdırır
print(df.index) #tablonun index değerlerini verir

"""
df2 = pd.DataFrame({
    "A":[1,2,3,4,5],
    "B":[10,20,30,40,50],
    "C":[100,200,300,400,500]
})
print(df2)
print(df2.T)

print(df.T)
print(df.sort_values(by ="total_rooms"))
print(df["total_rooms"].head())
print(df["total_rooms"][0:3])
print(df.loc[:,["total_rooms","population"]]) #sütunlar üzerinde çalışır
print(df.iloc[1:10,[1,2]]) #indexler üzerinde çalışır
print(df[df["total_rooms"]> 100])
print(df2)
print(df2.iloc[:,1]+ df2.iloc[:,2])
print(df2.iloc[:,1]- df2.iloc[:,2])
print(pd.concat( [df2.iloc[:,1],df2.iloc[:,2]],axis=1))

df3=df2.copy()
print(df3)