#belli bir bir sayı arasındaki bütün 5şe bölünebilen sayıları ekrana yaz

def besebolunebilme (a,b):
    for i in range(a,b+1):
        if i % 5==0:
            print(i)

besebolunebilme (1,100)





