#Faktöriyel Hesaplama
"""
0!=1     4!=24
1!=1     5!=120
2!=2     6!=720
3!=6
"""
n=int(input("Bir sayı giriniz:"))
carpım=1
i=1
while(i<=n):
    carpım*=i
    i+=1
print(carpım)