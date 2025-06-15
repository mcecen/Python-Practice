"""
    1 den 10 a kadar her satırda bir artırarak aşağıdaki şekli oluşturan kodu yazınız.

     Beklenen çıltı:

    1
    12
    123
    1234
    12345
    123456
    1234567
    12345678
    123456789
    12345678910
"""

for i in range(1,12):
    for j in range(1,i):
         print(j,end='')
    print()