"""
Kullanıcıdan alınan Stringin son karakteirini silip ekrana yazan python kodunu yazınız.

    Test Data:
    good

    Beklenen Çıktı:
    goo
"""
kelime = input("Kelime: ")
yeni_kelime = kelime[0:len(kelime)-1]
print(yeni_kelime)