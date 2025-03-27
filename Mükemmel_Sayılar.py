#Mükemmel Sayılar
"""Kendisi hariç pozitif tam bölenlerinin toplamı kendisine eşit olan sayılara
mükemmel sayılar denir."""

sayi=int(input("Bir sayı giriniz:"))
toplam=0
for i in range(1,sayi):
    if(sayi%i==0):
        toplam+=i

if(sayi==toplam):
    print(sayi,"mükemmel sayıdır.")
else:
    print(sayi,"mükemmel sayı değildir.")

