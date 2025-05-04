"""
    Kullanıcıdan alınan String kümesi içerisinde aranan String i bulan Kodu yazınız.

    Test Data:
    Python is easy

    Aranan String: is

    Bektenen Çıktı:
    True

    Aranan String: and

    Beklenen Çıktı:False
"""

data = "Python is easy"
aranacak_kelime = input("Aranacak kelimeyi giriniz: ")
if aranacak_kelime in data:
    print("Aradığınız", aranacak_kelime, "kelimesi",data,"içerisinde mevcut")
else:
    print("Aradığınız kelime mevcut değil")