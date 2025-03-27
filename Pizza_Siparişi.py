#Pizza Siparişi
"""
Küçük boy (S) pizza:40 TL
Orta boy (M) pizza: 50 TL
Büyük boy (L) pizza: 60 TL

Ekstra peynirin pizza boyutlarına göre fiyatlandırılması:
Küçük boy (S) pizzaya +5TL
Orta boy (M) ve büyük boy (L) pizzaya + 10 TL

İçecek istiyorsa +20 TL
"""

print("PYTHON PİZZA'YA HOŞGELDİNİZ!")
print("____________________________________________________________")


boyut=input("Pizza boyutunuz nasıl olsun?(S/M/L):")
if(boyut=="S" or boyut=="M" or boyut=="L"):
       peynir=input("Ekstra peynir ister misiniz?(E/H):")
       if(peynir=="E"or peynir=="H"):
           icecek = input("İçecek istiyor musunuz?(E/H):")
           if(icecek=="E"or icecek=="H"):
               if (boyut == 'S'):
                   if (peynir == 'E'):
                       if (icecek == 'E'):
                           print("Tutar:{}TL".format(40 + 5 + 20))
                       else:
                           print("Tutar:{}TL".format(40 + 5))
                   else:
                       if (icecek == 'E'):
                           print("Tutar:{}TL".format(40 + 20))
                       else:
                           print("Tutar:{}TL".format(40))

               elif (boyut == 'M'):
                   if (peynir == 'E'):
                       if (icecek == 'E'):
                           print("Tutar:{}TL".format(50 + 10 + 20))
                       else:
                           print("Tutar:{}TL".format(50 + 10))
                   else:
                       if (icecek == 'E'):
                           print("Tutar:{}TL".format(50 + 20))
                       else:
                           print("Tutar:{}TL".format(50))
               elif (boyut == 'L'):
                   if (peynir == 'E'):
                       if (icecek == 'E'):
                           print("Tutar:{}TL".format(60 + 10 + 20))
                       else:
                           print("Tutar:{}TL".format(60 + 10))
                   else:
                       if (icecek == 'E'):
                           print("Tutar:{}TL".format(60 + 20))
                       else:
                           print("Tutar:{}TL".format(60))

           else:
             print("Siparişiniz için eksik veya yanlış bilgi girdiniz!")

       else:
           print("Siparişiniz için eksik veya yanlış bilgi girdiniz!")

else:
    print("Siparişiniz için eksik veya yanlış bilgi girdiniz!")












