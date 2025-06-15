import random

def sayi_tahmin():
    hedef = random.randint(1, 100)
    tahmin_hakki = 7

    print("Sayı Tahmin Oyunu! 1-100 arasında bir sayı tuttum.")
    print(f"{tahmin_hakki} hakkınız var.")

    while tahmin_hakki > 0:
        try:
            tahmin = int(input("Tahmininizi girin: "))
            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
                continue

            if tahmin == hedef:
                print("Tebrikler! Bildiniz.")
                break
            elif tahmin < hedef:
                print("Daha yüksek bir sayı deneyin.")
            else:
                print("Daha düşük bir sayı deneyin.")

            tahmin_hakki -= 1
            print(f"Kalan hakkınız: {tahmin_hakki}")

        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    if tahmin_hakki == 0:
        print(f"Üzgünüm, hakkınız bitti. Tutulan sayı: {hedef}")

if __name__ == "__main__":
    sayi_tahmin()