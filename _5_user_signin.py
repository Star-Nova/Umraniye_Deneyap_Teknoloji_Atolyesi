kullanicisimleri=["Ali", "Ege"]

kullanicisifreleri=["123","456"]



def signin (name,password):

    if name in kullanicisimleri:
        print("Lütfen başka bir kullanıcı  adı veya şifresi giriniz.")
    else:
        kullanicisimleri.append(name)
        kullanicisifreleri.append(password)
        print(f"Sisteme başarıyla kayıt oldunuz.\n Kullanıcı adınız: {name} \n Şifreiz: {password} ")


while True:
    name = str(input("Lütfen kullanıcı adınzı giriniz:"))

    password = int(input("Lütfen şifrenizi giriniz:"))
    signin(name,password)
    break
def deleteuser (name,passowrd)
print(f"Sistemdeki kullanıcılar: {kullanicisimleri},\n {kullanicisifreleri}")
