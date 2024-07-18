#Konuşarak ses dosyaysı oluşturma
import sounddevice as sd
import wavio
import time

duration=5 #kaç saniye kayıt süresi yapılacağını gösterir
fs=20000 #saniyede kaç ses dalgası (frekans)
output_file_name= "ses dosyası.wav" #Kaydettiğin sesin dosya ismi
print("Kayıt Başlamıştır :D")
audio=sd.rec(int(duration*fs),samplerate=fs , channels=1,dtype="int16")
sd.wait()
#ses dosyasını kaydetme
wavio.write(output_file_name,audio,fs,sampwidth=2) #HER BİT 8E DENK GELİR O YÜZDEN 2 YAZDIK ÇÜNKÜ

print("Oynatılıyor...")
sd.play(audio,fs)
sd.wait()
print("İşlem tamamlandı")

data=wavio.read("ses dosyası.wav")
fs=data.rate
sd.play(data.data,fs)
sd.wait()