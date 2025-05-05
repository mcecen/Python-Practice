"""
Kullanıcı tarafından girilen bir yılın  artık yıl olup
olmadığını kontrol etmek için bir python Methodu yazınız.

    Test Data:
    2017

    Beklenen Çıktı:
    false
"""
yil = int(input("Yıl girin: "))

if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print(f"{yil} yılı artık yıldır.")

else:
    print(f"{yil} yılı artık yıl değildir.")