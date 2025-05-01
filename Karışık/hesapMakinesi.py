giris = """
(1) Toplama
(2) Cikarma
(3) Carpma
(4) Bolme
(5) Us Alma
(6) Karekok Hesaplama
"""
print(giris)

while True:
    soru = input("Yapmak istediğiniz islemin numarasını girin (Çıkmak için q ya da Q tuşuna basınız): ")
    if soru == "q" or soru =="Q":
        print("ÇIKIŞ YAPILDI...")
        break

    elif soru == "1":
        sayi1 = int(input("Toplama islemi icin ilk sayiyi girin: "))
        sayi2 = int(input("Toplama islemi icin ikinci sayiyi girin: "))
        print(sayi1, "+", sayi2, "=", sayi1 + sayi2)

    elif soru == "2":
        sayi3 = int(input("Cikarma islemi icin ilk sayiyi girin: "))
        sayi4 = int(input("Cikarma islemi icin ikinci sayiyi girin: "))
        print(sayi3, "-", sayi4, "=", sayi3 - sayi4)

    elif soru == "3":
        sayi5 = int(input("Carpma islemi icin ilk sayiyi girin: "))
        sayi6 = int(input("Carpma islemi icin ikinci sayiyi girin: "))
        print(sayi5, "x", sayi6, "=", sayi5 * sayi6)

    elif soru == "4":
        sayi7 = int(input("Bolme islemi icin ilk sayiyi girin: "))
        sayi8 = int(input("Bolme islemi icin ikinci sayiyi girin: "))
        print(sayi7, "/", sayi8, "=", sayi7 / sayi8)

    elif soru == "5":
        sayi9 = int(input("Ussu alinacak sayiyi girin: "))
        sayi10 = int(input("Us degerini girin: "))
        print(sayi9, "sayisinin", sayi10, "ussu=", sayi9**sayi10)

    elif soru == "6":
        sayi11 = int(input("Karekok hesaplamak istediginiz sayiyi girin: "))
        print(sayi11, "sayisinin karekoku = ", sayi11 ** 0.5)

    else:
        print("Yanlis giris.")
        print("Asagidaki seceneklerden birini giriniz:", giris)