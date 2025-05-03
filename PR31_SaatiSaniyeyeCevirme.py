"""
Saati saniyeye çeviren java methodunu yazınız.

    Test Data:
    howManySeconds(2);
    Beklenen çıktı:
     7200
"""


saat = int(input("Saat giriniz: "))
def howManySeconds(saat):
    dakika = saat*60
    saniye = dakika*60
    return saniye

print(howManySeconds(saat))