"""
Bir arrayi tersine çeviren  method yazınız.

    Test Data:

    reverse [1, 2, 3, 4]
    return  [4, 3, 2, 1]

"""
bos_list = []
sayac=10


for i in range(sayac):
    sayi = int(input("sayi giriniz: "))
    bos_list.append(sayi)

ters_liste=bos_list[::-1]
print(ters_liste)
