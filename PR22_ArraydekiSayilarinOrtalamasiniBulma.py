"""
Arraydeki sayıların ortalamasını hesaplayan Java Kodunu yazınız.

    Array =  [20, 30, 25, 35, -16, 60, -100 ]

    Beklenen Çıktı:
    Array Sayılarının ortalaması: 7.0
"""

liste = [20, 30, 25, 35, -16, 60, -100]
toplam = 0
for i in liste:
    toplam+=i
print("Ortalama: ", int(toplam/len(liste)))