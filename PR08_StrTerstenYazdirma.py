"""
     Girilen String değerde tersten yazan Python kodunu yazınız.

    Test Data:
    python
    nohtyp
"""

metin = input("Bir metin girin: ")

ters_metin = ""

i = len(metin) - 1
while i >= 0:
    ters_metin += metin[i]
    i -= 1
print("Tersten metin:", ters_metin)