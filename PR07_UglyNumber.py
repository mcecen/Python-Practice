"""
    Ugly Number:

    Girilen bir sayının  ugly number olup olmadığını kontrol etmek için bir program yazın.


    Sayı sisteminde,  ugly number  sadece asal faktörleri carpanlari 2, 3 veya 5 olan pozitif sayılardan olusur...
    İlk 10  ugly number 1, 2, 3, 4, 5, 6, 8, 9, 10, 12'dir. Kural olarak, 1 dahil.

    Test Data:
    13

    Beklenen çıktı:
    ugly number  degildir

    Test Data:
    25
    Beklenen Çıktı:

    ugly number
"""

sayi = int(input("Lütfen sayi giriniz: "))
if (sayi == 1 or sayi%2 ==0 or sayi%3 ==0 or sayi%5 ==0):
    print("Girilen sayi ugly sayidir")
else:
    print("Girilen sayi ugly degildir")