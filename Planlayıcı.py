#Planlayıcı

import os

dosya_adi = "planlayıcı.txt"


def dosya_olustur():
    """Planlayıcı dosyası yoksa oluştur."""
    if not os.path.exists(dosya_adi):
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            dosya.write(" Günlük Planlayıcı\n\n")


def gorev_ekle(görev):
    """Yeni bir görev ekle."""
    with open(dosya_adi, "a", encoding="utf-8") as dosya:
        dosya.write(f"- {gorev}\n")
    print("Görev eklendi!")


def gorevleri_listele():
    """Planlayıcıdaki görevleri listele."""
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        icerik = [satir.strip() for satir in dosya.readlines() if satir.strip()]  # Boş satırları temizle

    if len(icerik) <= 1:
        print("Planlayıcı şu an boş!")
        return

    print("\nGünlük Yapılacaklar Listesi:\n")

    for index, gorev in enumerate(icerik[1:], start=1):
        print(f"{index}. {gorev}")


def gorev_sil(no):
    """Belirtilen numaradaki görevi sil."""
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        gorevler = dosya.readlines()

    if 1 <= no < len(gorevler):
        silinen = gorevler.pop(no)
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            dosya.writelines(gorevler)
        print(f"{silinen.strip()} silindi!")
    else:
        print("Geçersiz görev numarası!")


# Program Çalıştırma
dosya_olustur()

while True:
    print(" PLANLAYICI MENÜSÜ ")
    print("1️)Görev Ekle")
    print("2) Görevleri Listele")
    print("3️) Görev Sil")
    print("4️) Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        gorev = input("Yeni görevi girin: ")
        gorev_ekle(gorev)
    elif secim == "2":
        gorevleri_listele()
    elif secim == "3":
        gorevleri_listele()
        try:
            no = int(input("Silmek istediğiniz görev numarasını girin: "))
            gorev_sil(no)
        except ValueError:
            print(" Lütfen geçerli bir sayı girin!")
    elif secim == "4":
        print("Çıkış yapıldı, görüşmek üzere!")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin!")


