"""
Karışık verilen sayıları  ve kelimeleri  sıralayan   Java kodunun yazınız.
    not: Test datadaki değerleri kullanınız.


    Test Data:
    [1232, 1134,2345,1022]
    [Java, Python, PHP, C#, C Programming, C++]

    Beklenen Çıktı:
    [1022,1134,1232,2345]
    [C Programming, C#, C++, Java, PHP, Python]
"""
liste1=  [1232, 1134,2345,1022]
liste2= ["C Programming", "C#", "C++", "Java", "PHP", "Python"]

print(sorted(liste1))
print(sorted(liste2))

