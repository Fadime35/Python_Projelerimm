#Obsesif Kompulsif Bozukluk

"""Bir rehabilitasyon merkezinde çalıştığınızı düşünün.Obsesif-kompulsif bozukluklardan
muzdarip hastalar olsun. Bu hastalar her gün bir blogda günlük planlarını yazması
isteniyor.Program bazı anahtar kelimeleri arayarak hastaları gözetim altında tutacak.
Bu kelimeler şunlar:
alışveriş, tekrar, kumar, içki, bahis, oyun, para
Eğer bu kelimelerden herhangi biri blog girdilerinde geçiyorsa ekrana şunu yazdır:
"Bu konuda gerçekten biriyle konuşmanız gerekiyor, veya".
Ve sonrasında daha önceden belirlenmiş ve bir listede tutulan öneri listesinden rastgele
bir öneri sunmasını istiyoruz
Diğer durumda ekrana şunu yazdırabilirsiniz:
"Bloğunuzu güncellediğiniz için teşekkürler."
"""
import random
from random import randint
okb=["alışveriş", "tekrar", "kumar", "içki", "bahis", "oyun", "para"]
oneri=["Yürüyüşe ne dersin?","Kitap oku","Müzik dinlemek ister misin?","Kahve içmek ister misin?","Spor yap","Uyku düzenini ayarla"]
blog=input("Günlük planlarınızı yazınız:")
yeni_blog=blog.split()
for i in okb:
    if(i in blog):
        print("Bu konuda gerçekten biriyle konuşmanız gerekiyor, veya")
        j = (randint(0, 5))
        print(oneri[j])
        break
else:
    print("Bloğunuzu güncellediğiniz için teşekkürler.")