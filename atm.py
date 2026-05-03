"""
Bir ATM programı yazmanız istenmektedir.
Başlangıç Durumu
Kullanıcının başlangıç bakiyesi: 1000 TL

Program Akışı
Program çalıştığında kullanıcıya sürekli aşağıdaki menü gösterilmelidir:

1 - Bakiye Görüntüle
2 - Para Çek
3 - Para Yatır
4 - Çıkış

Kullanıcı bir seçim yapar ve program bu seçime göre işlem gerçekleştirir.

İstenen Özellikler
1-Bakiye Görüntüleme
Kullanıcı mevcut bakiyesini görebilmelidir.

2-Para Çekme
Kullanıcı çekmek istediği miktarı girer.
Eğer:
Bakiye yeterliyse → para çekilir ve bakiye güncellenir
Bakiye yetersizse → hata mesajı verilir
Negatif veya 0 değer girilirse işlem yapılmamalıdır.

3-Para Yatırma
Kullanıcı yatırmak istediği miktarı girer.
Girilen miktar:
Pozitif ise → bakiyeye eklenir
Negatif veya 0 ise → hata mesajı verilir

4-Çıkış
Program sonlandırılır.

5-Geçersiz Seçim
Kullanıcı 1–4 dışında bir değer girerse:
“Geçersiz seçim” mesajı gösterilmelidir.

Program Kuralları
Program, kullanıcı çıkış seçeneğini seçene kadar sürekli çalışmalıdır.
Her işlemden sonra kullanıcı tekrar menüye yönlendirilmelidir.
Kullanıcıdan alınan sayısal değerler uygun veri tipine dönüştürülmelidir.

BONUS (Zorlayıcı)

Aşağıdaki özellikleri ekleyerek programı geliştirin:

Şifre Kontrolü
Doğru şifre: 1234
Kullanıcıya 3 deneme hakkı ver
3 yanlış girişte program sonlansın

Günlük Para Çekme Limiti
Kullanıcı en fazla 500 TL çekebilsin

İşlem Mesajları
Her işlemden sonra:
“İşlem başarılı” / “İşlem başarısız” gibi mesajlar göster

"""
import sys
girisMesaji = """
İŞLEMLER

1 - Bakiye Görüntüle
2 - Para Çek
3 - Para Yatır
4 - Çıkış
"""

print(girisMesaji)
bakiye=5000
gunlukLimit=500
sifre=1234

for i in range(3):
    girilenSifre = int(input("Şifrenizi giriniz: "))

    if not girilenSifre:
        print("Parola boş geçilemez")
    
    elif i==2:
        print("parolayı 3 kez yanlış girdiniz.")
        break
    
    elif girilenSifre==sifre:

        while True:
            islemNumara=int(input("Yapacağınız işlemin numarasını seçin: "))

            if islemNumara not in range(1,5):
                print("Geçersiz işlem")
                break
    
            elif islemNumara==1:
                print("İşlem başarılı")
                print("Hesap bakiyeniz: ",bakiye)

            elif islemNumara==2:
                cekimTutar=int(input("Çekmek istediğiniz tutarı giriniz: "))
        
                if bakiye>0 and bakiye>cekimTutar:
                    bakiye-=cekimTutar
                    print("İşlem başarılı")
                    print("Yeni Hesap bakiyeniz: ",bakiye)
                else:
                    print("Bakiye yeteriz. İşlem reddedildi")

            elif islemNumara==3:
                yatirilacakTutar=int(input("Yatırmak istediğiniz tutarı giriniz: "))
                bakiye+=yatirilacakTutar
                print("İşlem başarılı")
                print("Yeni Hesap bakiyeniz: ",bakiye)
    
            elif islemNumara==4:
                print("Çıkış yapılıyor...")
                sys.exit()