dictionary = {
    "cool": "havalı",
    "cevap": "yanıt",
    "detay": "ayrıntı",
    "isim": "ad",
    "random": "rastgele",
    "anormal": "olağan dışı"
}

cumle = input("Lütfen bir tümce giriniz: ")
kelimeler = cumle.split(" ")

ozturkce = ""

for kelime in kelimeler:
    if kelime in dictionary:
        ozturkce += dictionary[kelime] + " "
    else:
        ozturkce += kelime + " "

print(ozturkce.strip())  # strip() fonksiyonu ile baştaki ve sondaki fazla boşlukları kaldırıyoruz

