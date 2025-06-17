import pygame
import sys
import random
import time

# Pygame'i başlat
pygame.init()

# --- Oyun Ayarları ve Sabitler ---
GENISLIK, YUKSEKLIK = 800, 600
BLOK_BOYUTU = 20

# Renkler (RGB)
SIYAH = (15, 15, 15)  # Daha yumuşak bir siyah
BEYAZ = (255, 255, 255)
YESIL = (40, 180, 99)
ACIK_YESIL = (120, 220, 150)  # Demo yılan için
KIRMIZI = (220, 30, 30)
MAVI = (50, 153, 213)
SARI_VURGU = (241, 196, 15)

# Ekranı ve saati oluştur
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption('Python Yılan Oyunu')
saat = pygame.time.Clock()

# Fontlar
font_baslik = pygame.font.SysFont('impact', 70)
font_menu = pygame.font.SysFont('corbel', 40)
font_talimat = pygame.font.SysFont('calibri', 22, italic=True)
skor_font = pygame.font.SysFont('comicsansms', 35)

def skoru_goster(skor, hiz):
    """Anlık skoru ve hızı ekranda gösterir."""
    skor_metni = skor_font.render(f"Skor: {skor}", True, BEYAZ)
    hiz_metni = skor_font.render(f"Hız: {hiz}", True, BEYAZ)
    ekran.blit(skor_metni, [10, 10])
    ekran.blit(hiz_metni, [GENISLIK - 150, 10])

def yilan_ciz(yilan_listesi, yilan_rengi=YESIL):
    """Yılanın her bir parçasını ekrana çizer."""
    for x in yilan_listesi:
        pygame.draw.rect(ekran, yilan_rengi, [x[0], x[1], BLOK_BOYUTU, BLOK_BOYUTU])

def metin_nesnesi(text, font, color):
    """Verilen metni render eder."""
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def mesaj_goster(text, renk, y_offset=0, boyut='buyuk'):
    """Ekrana ortalanmış mesaj gösterir (Oyun sonu ekranı için)."""
    if boyut == 'buyuk':
        font = pygame.font.SysFont('corbel', 50, bold=True)
    else:
        font = pygame.font.SysFont('corbel', 30)

    TextSurf, TextRect = metin_nesnesi(text, font, renk)
    TextRect.center = ((GENISLIK / 2), (YUKSEKLIK / 2) + y_offset)
    ekran.blit(TextSurf, TextRect)

def baslangic_ekrani():
    """Daha görsel ve etkileşimli başlangıç menüsü."""
    menu_aktif = True
    secili_opsiyon = 0
    opsiyonlar = ["Kolay", "Normal", "Zor"]
    hiz_degerleri = [10, 15, 25]

    # Arka planda hareket eden demo yılan için ayarlar
    demo_yilan = [[100, 100], [80, 100], [60, 100]]
    demo_yon = [BLOK_BOYUTU, 0]  # Sağa doğru hareket

    while menu_aktif:
        # --- Olay Yönetimi (Tuş Basımları) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    secili_opsiyon = (secili_opsiyon - 1) % len(opsiyonlar)
                elif event.key == pygame.K_DOWN:
                    secili_opsiyon = (secili_opsiyon + 1) % len(opsiyonlar)
                elif event.key == pygame.K_RETURN:  # ENTER tuşu
                    return hiz_degerleri[secili_opsiyon]

        # --- Demo Yılan Mantığı ---
        # Yılanın başını hareket ettir
        yeni_bas = [demo_yilan[0][0] + demo_yon[0], demo_yilan[0][1] + demo_yon[1]]

        # Duvarlara çarpınca yön değiştir
        if yeni_bas[0] >= GENISLIK or yeni_bas[0] < 0:
            demo_yon[0] *= -1
            if random.choice([True, False]): demo_yon = [0, BLOK_BOYUTU * (-1 if demo_yon[0] > 0 else 1)]
        if yeni_bas[1] >= YUKSEKLIK or yeni_bas[1] < 0:
            demo_yon[1] *= -1
            if random.choice([True, False]): demo_yon = [BLOK_BOYUTU * (-1 if demo_yon[1] > 0 else 1), 0]

        yeni_bas = [demo_yilan[0][0] + demo_yon[0], demo_yilan[0][1] + demo_yon[1]]
        demo_yilan.insert(0, yeni_bas)
        demo_yilan.pop()

        # --- Çizim Kodları ---
        ekran.fill(SIYAH)
        yilan_ciz(demo_yilan, ACIK_YESIL)  # Demo yılanı çiz

        # Başlık
        baslik_surf, baslik_rect = metin_nesnesi("YILAN OYUNU", font_baslik, SARI_VURGU)
        baslik_rect.center = (GENISLIK / 2, YUKSEKLIK / 4)
        ekran.blit(baslik_surf, baslik_rect)

        # Menü seçenekleri
        for i, opsiyon_metni in enumerate(opsiyonlar):
            y_pozisyonu = YUKSEKLIK / 2 + i * 60
            if i == secili_opsiyon:
                renk = YESIL
                # Seçili olana > işareti ekle
                secim_isareti, _ = metin_nesnesi(">", font_menu, renk)
                ekran.blit(secim_isareti, (GENISLIK / 2 - 120, y_pozisyonu - 25))
            else:
                renk = BEYAZ

            opsiyon_surf, opsiyon_rect = metin_nesnesi(opsiyon_metni, font_menu, renk)
            opsiyon_rect.center = (GENISLIK / 2, y_pozisyonu)
            ekran.blit(opsiyon_surf, opsiyon_rect)

        # Talimatlar
        talimat_surf, talimat_rect = metin_nesnesi("Seçmek için YÖN TUŞLARI, onaylamak için ENTER", font_talimat, MAVI)
        talimat_rect.center = (GENISLIK / 2, YUKSEKLIK - 50)
        ekran.blit(talimat_surf, talimat_rect)

        pygame.display.update()
        saat.tick(15)  # Menü animasyon hızı

def oyun_dongusu(baslangic_hizi):
    """Ana oyun döngüsü."""
    oyun_bitti = False
    oyun_kapandi = False

    # Yılanın başlangıç pozisyonu ve hızı
    x1 = GENISLIK / 2
    y1 = YUKSEKLIK / 2
    x1_degisim = 0
    y1_degisim = 0

    yilan_listesi = []
    yilan_uzunlugu = 1
    hiz = baslangic_hizi

    # Yemin başlangıç pozisyonu
    yem_x = round(random.randrange(0, GENISLIK - BLOK_BOYUTU) / BLOK_BOYUTU) * BLOK_BOYUTU
    yem_y = round(random.randrange(0, YUKSEKLIK - BLOK_BOYUTU) / BLOK_BOYUTU) * BLOK_BOYUTU

    while not oyun_bitti:

        while oyun_kapandi:
            ekran.fill(MAVI)
            mesaj_goster("Oyun Bitti!", KIRMIZI, -50, 'buyuk')
            mesaj_goster(f"Final Skor: {yilan_uzunlugu - 1}", BEYAZ, 20, 'kucuk')
            mesaj_goster("Ana Menüye Dönmek İçin Bir Tuşa Basın", BEYAZ, 80, 'kucuk')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return  # Oyun döngüsünden çıkarak ana menüye dön
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # --- Olayları (Klavye Girişleri) Yönet ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyun_bitti = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if x1_degisim == BLOK_BOYUTU: continue
                    x1_degisim = -BLOK_BOYUTU
                    y1_degisim = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if x1_degisim == -BLOK_BOYUTU: continue
                    x1_degisim = BLOK_BOYUTU
                    y1_degisim = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if y1_degisim == BLOK_BOYUTU: continue
                    y1_degisim = -BLOK_BOYUTU
                    x1_degisim = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if y1_degisim == -BLOK_BOYUTU: continue
                    y1_degisim = BLOK_BOYUTU
                    x1_degisim = 0

        # --- Oyun Mantığı ---
        if x1 >= GENISLIK or x1 < 0 or y1 >= YUKSEKLIK or y1 < 0:
            oyun_kapandi = True

        x1 += x1_degisim
        y1 += y1_degisim

        # --- Çizim Kodları ---
        ekran.fill(SIYAH)
        pygame.draw.rect(ekran, KIRMIZI, [yem_x, yem_y, BLOK_BOYUTU, BLOK_BOYUTU])

        yilan_basi = [x1, y1]
        yilan_listesi.append(yilan_basi)

        if len(yilan_listesi) > yilan_uzunlugu:
            del yilan_listesi[0]

        for x in yilan_listesi[:-1]:
            if x == yilan_basi:
                oyun_kapandi = True

        yilan_ciz(yilan_listesi)
        skoru_goster(yilan_uzunlugu - 1, hiz)
        pygame.display.update()

        # Yılan yemi yedi mi?
        if x1 == yem_x and y1 == yem_y:
            yem_x = round(random.randrange(0, GENISLIK - BLOK_BOYUTU) / BLOK_BOYUTU) * BLOK_BOYUTU
            yem_y = round(random.randrange(0, YUKSEKLIK - BLOK_BOYUTU) / BLOK_BOYUTU) * BLOK_BOYUTU
            yilan_uzunlugu += 1

            if (yilan_uzunlugu - 1) % 3 == 0:
                hiz += 1

        saat.tick(hiz)

    pygame.quit()
    sys.exit()

# Ana program döngüsü
if __name__ == "__main__":
    while True:
        secilen_hiz = baslangic_ekrani()
        oyun_dongusu(secilen_hiz)