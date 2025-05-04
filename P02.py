"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
sayi = int(input("Sayi giriniz: "))
def faktoriyel(sayi):
    if sayi == 0:
        return 1
    return sayi*faktoriyel(sayi-1)

print(faktoriyel(sayi))

#---------------------
sayi = int(input("Sayı : "))

faktoriyel = 1

if sayi<0:
    print("Negatif sayıların faktoriyeli hesaplanamaz")
elif sayi==0:
    print("Sonuç : 1")
else:
    for i in range(1,sayi+1):
        faktoriyel = faktoriyel * i
    print("Sonuç : ",faktoriyel)
