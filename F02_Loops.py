print("🎓 Sınıf Not İşleme Programı (Döngülerle)")

# 1. Temel for döngüsü ile öğrenci listesi yazdırma
ogrenciler = ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"]
print("\n📋 Sınıftaki Öğrenciler:")
for isim in ogrenciler:
    print("-", isim)

# 2. for döngüsü ile indisli yazdırma (range + len)
print("\n📋 İndisli Liste:")
for i in range(len(ogrenciler)):
    print(f"{i + 1}. öğrenci: {ogrenciler[i]}")

# 3. Öğrenci notlarını kullanıcıdan alma (while döngüsü)
notlar = []
i = 0
print("\n📝 Öğrenci notlarını girin (0-100 arası):")
while i < len(ogrenciler):
    try:
        not_girisi = float(input(f"{ogrenciler[i]} notu: "))
        if 0 <= not_girisi <= 100:
            notlar.append(not_girisi)
            i += 1
        else:
            print("⚠️ Lütfen 0-100 arasında bir not girin.")
    except ValueError:
        print("❌ Sayısal bir değer girin.")

# 4. notlara göre değerlendirme (for döngüsü ve koşul)
print("\n📊 Not Değerlendirmesi:")
for i in range(len(ogrenciler)):
    durum = ""
    if notlar[i] >= 85:
        durum = "Pekiyi"
    elif notlar[i] >= 70:
        durum = "İyi"
    elif notlar[i] >= 50:
        durum = "Orta"
    else:
        durum = "Başarısız"
    print(f"{ogrenciler[i]}: {notlar[i]} - {durum}")

# 5. notu 90'dan yüksek olan ilk öğrenciyi bul (break)
print("\n🔍 90 üstü ilk notu bulan öğrenci:")
for i in range(len(notlar)):
    if notlar[i] > 90:
        print(f"{ogrenciler[i]} - {notlar[i]}")
        break
else:
    print("Hiçbir öğrenci 90'dan yüksek almadı.")

# 6. Ortalamanın altında kalanları atla (continue)
ortalama = sum(notlar) / len(notlar)
print(f"\n📈 Sınıf Ortalaması: {ortalama:.2f}")
print("📌 Ortalamanın üstünde olanlar:")
for i in range(len(notlar)):
    if notlar[i] < ortalama:
        continue
    print(f"{ogrenciler[i]}: {notlar[i]}")

# 7. İç içe for döngüsü ile çarpım tablosu (ekstra örnek)
print("\n🧮 1'den 5'e kadar çarpım tablosu:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j}", end="\t")
    print()  # Satır atla
