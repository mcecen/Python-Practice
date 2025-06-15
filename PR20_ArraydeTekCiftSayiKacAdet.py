"""
Array içerisindeki tek ve çift sayıların
    kaçar tane olduğunu bulan Python Kodu yazınız.

    Array: [1,2,3,4,5,6,7,8,9]

    Beklenen Çıktı:

    Tek Sayilar: 5
    Cift Sayilar: 4
"""

liste = range(100)
liste2 = [1,2,3,4,5,6,7,8,9]

tekSayiSayac = 0
ciftSayiSayac = 0
for i in liste:
    if liste[i-1] % 2 == 0:
        ciftSayiSayac += 1

    elif liste[i-1] % 2 != 0:
        tekSayiSayac += 1
    else:
        print("Hatalı değer girildi")
print("Çift sayıların sayısı: ",ciftSayiSayac)
print("Tek sayıların sayısı: ",tekSayiSayac)