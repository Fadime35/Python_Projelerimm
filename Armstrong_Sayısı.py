#Armstrong Sayısı
"""Tüm basamaklarındaki rakamların sayı değerlerinin küpleri toplamı,
kendisine eşit olan sayılara "Armstrong sayısı"denir. """

sayi=int(input("Bir sayı giriniz:"))
toplam=0
for i in str(sayi):
    toplam+=int(i)**3

if(toplam==sayi):
    print(sayi,"armstrong sayısıdır.")
else:
    print(sayi,"armstrong sayısı değildir.")











