"""
Array deki sayıları tolpayan Java kodunu yazınız.

    array  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Beklenen Çıktı:
    Array toplamı: 55
"""
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toplam=0
for i in liste:
    toplam+=i
print("Toplam: ",toplam)