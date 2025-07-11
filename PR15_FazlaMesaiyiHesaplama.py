"""
Fazla mesaiyi hesaplayan bir program yazınız.
    Yazacağınız program toplam kazancı return etsin.

    Kullanıcıdan saatlik çalışma ücretini, hangi saatler arasında çalıştığını ve
    fazla mesaiye kalırsa kazancını kaç ile katlayacağını alalım.

    Daha sonra şu şekilde bir program yazınız :

    Örnek :
    saatlik çalışma ücreti : 40.0
    hangi saat başladı : 9.0
    hangi saat bitti : 20.0
    mesaiyi kaçla katlayacağız : 1.8

    ucretHesapla(9.0,20.0,40.0,1.8);

    9 ile 17 arasında toplam çalışma 8 saat olduğu için 8 x 40 = 320
    17 ile 20 arasında toplam çalışma 3 saat olduğu için 3 x 40 x 1.8 =  216

    toplam = 536.0
"""

def ucretHesapla(baslangicSaat,bitisSaat,saatlikUcret,mesaiKatSayisi):
    normalMesaiBitisSaat = 17
    toplamUcret = 0

    # Normal mesai saati: 9.0 - 17.0 arası
    if baslangicSaat < normalMesaiBitisSaat:
        normalSaat = min(bitisSaat, normalMesaiBitisSaat) - baslangicSaat
        toplamUcret += normalSaat * saatlikUcret
    else:
        normalSaat = 0

    #Fazla mesai saati: 17.0 sonrası

    if bitisSaat > normalMesaiBitisSaat:
        mesaiSaat = bitisSaat - max(baslangicSaat,normalMesaiBitisSaat)
        toplamUcret += mesaiSaat * saatlikUcret * mesaiKatSayisi
    else:
        mesaiSaat = 0

    return toplamUcret

ucret = ucretHesapla(9.0, 20.0, 40.0, 1.8)
print(f"Toplam kazanç: {ucret}")