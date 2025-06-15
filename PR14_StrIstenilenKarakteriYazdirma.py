"""
 Gİrilen String değer içinde istenen sıradaki karakteri bulan python kodunu yazınız.

    Test Data:
    Python is fun

    Beklenen Çıktı
    0. pozisyondaki karakter : J

    5. pozisyondaki karakter : i
"""
kelime = input("Kelime: ")
istenen_kelime_indisi = int(input("Istenen kelime indisi: "))

if istenen_kelime_indisi > len(kelime):
    print("istenen indis kelime uzunluğundan fazla")
else:
    print(kelime[istenen_kelime_indisi])