#Sayı Tahmin Oyunu

"""Bilgisayar 1 ile 50 arasında bir sayı tutar.Kullanıcıdan tahmin
değer istenir.Kullanıcının 10 deneme hakkı vardır.Bu uygulamada 100
üzerinden puanlama sistemi vardır.Her tahmin 10 puandır.
"""
import random
bilgisayar=random.randint(1,50)
puan=100
hak=0
while(hak<10):
    tahmin = int(input("Aklınızdan bir sayı tutun:"))
    if(tahmin<bilgisayar):
        print("Daha büyük değer girmelisiniz!")
        puan-=10
        hak+=1
    elif(tahmin>bilgisayar):
        print("Daha küçük değer girmelisiniz!")
        puan -= 10
        hak += 1
    else:
        print(f"Tebrikler!\n{hak+1}.denemenizde doğru bildiniz.")
        print("Puanınız:",puan)
        break






