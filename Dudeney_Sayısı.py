#Dudeney Sayısı
"""Dudeney sayısı,basamaklarının sayı değerleri toplamının küpü kendisine
eşit olan sayıdır."""

sayi=input("Bir sayı giriniz:")
toplam=0

for i in sayi:
    toplam+=int(i)

dudeney_mi=toplam**3
if(dudeney_mi==int(sayi)):
    print(sayi,"dudeney sayısıdır.")
else:
    print(sayi,"dudeney sayısı değildir.")




