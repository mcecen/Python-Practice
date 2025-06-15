"""
RG01_BasamakDegerleriToplami
/*1---
    Sayinin Sayi degerlerinin toplamasini yapan kodu yaziniz.

    Test Data
    34
    Beklenen Cikti
    7
    */
"""

# Kullanıcıdan sayı al
sayi = int(input("Bir sayı girin: "))

# Basamakların toplamını hesapla
toplam = 0
for basamak in str(sayi):
    toplam += int(basamak)

# Sonucu yazdır
print("Basamak sayılarının toplamı:", toplam)

