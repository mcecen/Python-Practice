"""
Bir palindrom, madam veya racecar veya 10801 sayısı gibi
    ileriye doğru geriye doğru okuyan bir kelime, sayı, kelime öbeği veya diğer karakter dizisidir.

    Girilecek kelimenin palindrom olup olmadığını doğrulayacak bir python Kodu yazın.

    Test Data:
    madam

    Beklenen Çıktı:
    True
"""
kelime = input("Kelime: ")
ters_kelime=""
kelime_uzunlugu=len(kelime)-1

while kelime_uzunlugu>=0:
    ters_kelime += kelime[kelime_uzunlugu]
    kelime_uzunlugu -= 1

if ters_kelime == kelime:
    print("Kelime palindrom")
else:
    print("Kelime palindrom değil")