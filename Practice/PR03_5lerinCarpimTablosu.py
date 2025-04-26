"""
    Belirlenen sayının 1 den 10 a kadar çarpım sonuçlarını yapan programı yazınız.

    Örnek Sonuç:
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25
    5 x 6 = 30
    5 x 7 = 35
    5 x 8 = 40
    5 x 9 = 45
    5 x 10 = 50
"""

sayi = int(input("Sayi giriniz:  "))

for i in range(1,11):
    print(sayi," x ",i, " = ", sayi*i)