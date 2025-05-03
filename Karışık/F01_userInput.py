# Giriş ekranı
print("=" * 50)
print("📋 KULLANICI BİLGİ SİSTEMİ".center(50))
print("=" * 50)

# input() kullanarak kullanıcıdan bilgi alalım
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
yas = int(input("Yaşınız: "))
meslek = input("Mesleğiniz: ")
maas = float(input("Aylık maaşınız (₺): "))
vergi_orani = float(input("Vergi oranı (% olarak): "))

# Karakter kaçışları
print("\nİşleniyor...\n")

# B. KART: Biçimlendirilmiş kullanıcı kartı
print("=" * 50)
print("🪪 KULLANICI KARTI")
print("=" * 50)

# Metin hizalama: solda, ortada, sağda
print("{:<15}: {}".format("Ad Soyad", f"{ad.capitalize()} {soyad.upper()}"))
print("{:<15}: {:>3} yaş".format("Yaş", yas))
print("{:<15}: {:^20}".format("Meslek", meslek.title()))
print("{:<15}: {:,.2f} ₺".format("Maaş", maas))

# Vergi hesaplama ve yüzde gösterimi
vergi_tutar = maas * (vergi_orani / 100)
net_maas = maas - vergi_tutar

print("{:<15}: {:.2f} %".format("Vergi Oranı", vergi_orani))
print("{:<15}: {:,.2f} ₺".format("Net Maaş", net_maas))

print("=" * 50)

# C. print() ile sep ve end parametreleri
print("\n🖨️ Örnek: print() ile sep ve end kullanımı")
print("Ad", "Soyad", "Yaş", sep=" | ", end=" => ")
print(ad, soyad, yas, sep=" - ")

# D. Çok satırlı açıklama metni (triple quote)
print("""
📌 AÇIKLAMA:
- Bu sistem, girilen bilgileri biçimlendirerek raporlar.
- Sayılar para birimi gibi yazılır (₺, %).
- Metinler hizalanır: sola, sağa, ortalanır.
- print() → satır kontrolü ve ayırıcılar gösterildi.
""")

# E. Sayı formatları: Onluk, yüzde, binlik
print("📐 Sayı Biçimlendirme Örnekleri:")
deger = 1234567.89123
print("Ondalık   : {:.2f}".format(deger))
print("Yüzde     : {:.1%}".format(0.175))   # 17.5%
print("Binlik    : {:,}".format(9876543))   # 9,876,543

# F. Kullanıcı tablosu (sadece görsel amaçlı)
print("\n📊 Kullanıcı Tablosu")
print("-" * 50)
print("{:<15} {:<15} {:>10}".format("Ad", "Soyad", "Maaş (₺)"))
print("{:<15} {:<15} {:>10,.2f}".format(ad.capitalize(), soyad.capitalize(), maas))
print("-" * 50)