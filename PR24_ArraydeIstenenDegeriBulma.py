"""
Yazılan değerin array içerisinde arayan Java Kodu yazınız.

    Array: [1551,1223,1443,1267,1789,1023,2020]


    Aranan Değer:2020
    Beklenen Çıktı:True

    Aranan Değer:2010
    Beklenen Çıktı :False
"""
liste = [1551,1223,1443,1267,1789,1023,2020]
sayi = int(input("Aranacak sayiyi giriniz: "))

if sayi in liste:
    print("Aranan sayi listede mevcut")
else:
    print("Aranan sayi listede mevcut değil")