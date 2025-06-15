"""
Üç sayı arasındaki en küçük sayıyı bulmak için bir Python METHOD yazın.

    Test data:
    12,24,34

    Beklenen Çıktı:
    12
"""
ilk_sayi = int(input("İlk sayiyi giriniz: "))
ikinci_sayi = int(input("İkinci sayiyi giriniz: "))
ucuncu_sayi = int(input("Üçüncü sayiyi giriniz: "))

en_buyuk = ilk_sayi

def enBuyuk(ilk_sayi,ikinci_sayi,ucuncu_sayi):

    if ilk_sayi>ikinci_sayi and ilk_sayi>ucuncu_sayi:
        en_buyuk=ilk_sayi
        print("En büyük sayi: ",en_buyuk)

    elif ikinci_sayi>ilk_sayi and ikinci_sayi>ucuncu_sayi:
        en_buyuk = ikinci_sayi
        print("En büyük sayi: ",en_buyuk)

    else:
        en_buyuk = ucuncu_sayi
        print("En büyük sayi: ",en_buyuk)

enBuyuk(ilk_sayi,ikinci_sayi,ucuncu_sayi)
