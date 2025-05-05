"""
Girilen Stringdeki tüm sesli harfleri saymak için bir python Methodu yazınız.

    Test Data:
    python is fun

    Beklenen Çıktı:

    Stringdeki sesli harf sayısı: 4
"""
sesli_sayi=0
kelime = input("Cümle giriniz: ")
for i in kelime:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="ı" or i=="ü" or i=="ö":
        sesli_sayi=sesli_sayi+1
print("Girilen cümledeki sesli harf sayisi: ", sesli_sayi)
