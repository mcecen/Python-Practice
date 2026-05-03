"""
Soru: Kapsamlı Karar Destek Sistemi

1. Veri Validasyonu (Giriş Katmanı)
Program, kullanıcıdan aşağıdaki verileri almalı ve hatalı girişlere karşı dirençli olmalıdır:

Yaş: Tam sayı (Integer).
Çalışma Durumu: String (E/H).

2. Segmentasyon Mantığı
Program, verileri aşağıdaki hiyerarşiye göre analiz etmelidir:

A. Geçersiz Veri Kontrolü
Yaş 0'dan küçükse veya 120'den büyükse: "Hatalı yaş girişi yapıldı." mesajı verilmeli ve program sonlanmalıdır.

B. Reşit Olmayanlar Segmenti (Yaş < 18)
Bu grupta çalışma durumu sorgulanmaz, sadece yaş bazlı alt segmentlere bakılır:

0 - 12 Yaş: "Çocukluk dönemi segmenti"
13 - 15 Yaş: "Erken ergenlik dönemi segmenti"
16 - 17 Yaş: "Genç birey segmenti"

C. Yetişkinler Segmenti (18 ≤ Yaş ≤ 65)
Bu grupta kararlar, yaş ve çalışma durumunun kombinasyonuna göre verilir:

Çalışıyor ise:
18 - 24 Yaş: "Junior / Akademik Gelişim Süreci"
25 - 40 Yaş: "Mid-Level / Aktif Kariyer Yönetimi"
41 - 65 Yaş: "Senior / Stratejik Deneyim Dönemi"

Çalışmıyor ise: 
"Kariyer Planlama veya Eğitim Aşamasında"

D. Emeklilik Segmenti (Yaş > 65)

Çalışıyor ise: 
"Aktif Yaşlanma ve Danışmanlık Süreci"

Çalışmıyor ise: 
"Emeklilik ve Sosyal Dinlenme Dönemi"

"""
import sys
yas = int(input("Yaşınızı tam sayı olarak giriniz: "))
calismaDurumu = input("Çalışma durumunuzu E veya H olarak giriniz: ")

if yas<0 or yas>120:
    print("Hatalı yaş girişi yapıldı")
    sys.exit()

elif yas>0 and yas<13:
    print("Çocukluk dönemi segmenti")

elif yas>=13 and yas<15:
    print("Erken ergenlik dönemi segmenti")

elif yas>=16 and yas<17:
    print("Genç birey segmenti")

elif yas>=18 and yas<=65:

    if calismaDurumu.upper()=="E":
        if yas>=18 and yas<24:
            print("Junior / Akademik Gelişim Süreci")
        
        elif yas>=25 and yas<40:
            print("Mid-Level / Aktif Kariyer Yönetimi")
        
        else:
            print("Senior / Stratejik Deneyim Dönemi")
    
    if calismaDurumu.upper()=="H":
        print("Kariyer Planlama veya Eğitim Aşamasında")

elif yas>65:

    if calismaDurumu.upper()=="E":
        print("Aktif Yaşlanma ve Danışmanlık Süreci")
    
    if calismaDurumu.upper()=="H":
        print("Emeklilik ve Sosyal Dinlenme Dönemi")
else:
    print(":)")