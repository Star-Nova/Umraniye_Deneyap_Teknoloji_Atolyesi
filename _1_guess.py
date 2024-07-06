import random

hak = 10

guess_number = random.randint(1, 100)
print("1 ile 100 arasında bir sayı tahmin et!")

while True:

        guess = int(input("Tahmininiz: "))
        hak -= 1
        if guess < guess_number:
            print("Daha büyük bir sayı tahmin edin. -_-")

        elif guess > guess_number:
            print("Daha düşük bir sayı tahmin edin. o_O")
        else:
            print(f"Tebrikler! {guess_number} sayısını doğru tahmin ettiniz :)")
            break

        if hak==0:
            print("Oyun Bitti Kaybettiniz")
            break

guess_number()
