"""
    Aşağıdaki elmas deseni görüntüsünü çizen kodu yazınız.
    Test Data:
    Yarım elmas uzunluğu : 7
    Beklenen Çıktı:
          *
         ***
        *****
       *******
      *********
     ***********
    *************
     ***********
      *********
       *******
        *****
         ***
          *
"""
sayi = int(input("Elmas için sayi giriniz:"))

# Üst yarı (orta satıra kadar)
for i in range(sayi):
    bosluk = sayi - i - 1
    yildiz = 2 * i + 1
    print(" " * bosluk + "*" * yildiz)

# Alt yarı
for i in range(sayi - 2, -1, -1):
    bosluk = sayi - i - 1
    yildiz = 2 * i + 1
    print(" " * bosluk + "*" * yildiz)