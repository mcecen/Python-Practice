import time
import sys

def geri_sayim_gorsel(dakika):
    """Konsoldan alinan dakikayi, bir ilerleme çubuğu ile görsel olarak geriye sayar."""
    toplam_saniye = dakika * 60

    # İlerleme çubuğunun genişliği (karakter sayısı)
    bar_uzunlugu = 50

    for i in range(toplam_saniye, -1, -1):
        kalan_saniye = i
        d = kalan_saniye // 60
        s = kalan_saniye % 60

        # Geçen sürenin yüzdesini hesapla
        yuzde = (toplam_saniye - kalan_saniye) / toplam_saniye

        # İlerleme çubuğunu oluştur
        dolu_kisim = int(yuzde * bar_uzunlugu)
        bar = '█' * dolu_kisim + '-' * (bar_uzunlugu - dolu_kisim)

        # Ekrana yazdır
        # sys.stdout.write kullanmak, print'ten daha stabil bir satır güncellemesi sağlar
        sys.stdout.write(f"\rKalan Süre: {d:02d}:{s:02d} |{bar}| {int(yuzde * 100)}%")
        sys.stdout.flush()

        # Bir saniye bekle
        time.sleep(1)

    print("\nSüre doldu! :)")

# Kullanıcıdan dakika bilgisini al
try:
    dakika_girdisi = int(input("Geri sayım için dakika girin: "))
    if dakika_girdisi > 0:
        geri_sayim_gorsel(dakika_girdisi)
    else:
        print("Lütfen 0'dan büyük bir değer girin.")
except ValueError:
    print("Lütfen geçerli bir sayı girin.")