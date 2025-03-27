#Vize-Final Ortalama Hesaplama
"""
 Puan          Harf Notu                   Durumu
90-100           AA                       Başarılı
85-89            BA                       Başarılı
80-84            BB                       Başarılı
70-79            CB                       Başarılı
60-69            CC                       Başarılı
50-59            DC                       Başarısız
40-49            DD                       Başarısız
0-40             FF                       Başarısız
"""


vize=int(input("Vize notunuzu giriniz:"))
final=int(input("Final notunuzu giriniz:"))
ortalama=vize*0.4+final*0.6

if(90<=ortalama<=100):
    print("AA aldınız.\nDurum:Başarılı")
elif(85<=ortalama<90):
    print("BA aldınız.\nDurum:Başarılı")
elif(80<=ortalama<85):
    print("BB aldınız.\nDurum:Başarılı")
elif(70<=ortalama<80):
    print("CB aldınız.\nDurum:Başarılı")
elif(60<=ortalama<70):
    print("CC aldınız.\nDurum:Başarılı")
elif(50<=ortalama<60):
    print("DC aldınız.\nDurum:Başarısız")
elif(40<=ortalama<50):
    print("DD aldınız.\nDurum:Başarısız")
else:
    print("FF aldınız.\nDurum:Başarısız")
