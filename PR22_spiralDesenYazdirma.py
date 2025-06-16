def spiral_deseni_olustur(n):
    # n x n boyutunda boş matris oluştur
    matris = [[0]*n for _ in range(n)]

    # Spiral yazma için başlangıç değerleri
    sayi = 1
    sol = 0
    sag = n - 1
    ust = 0
    alt = n - 1

    while sol <= sag and ust <= alt:
        # Üst satırı sola doğru yaz
        for i in range(sol, sag+1):
            matris[ust][i] = sayi
            sayi += 1
        ust += 1

        # Sağ sütunu aşağıya doğru yaz
        for i in range(ust, alt+1):
            matris[i][sag] = sayi
            sayi += 1
        sag -= 1

        # Alt satırı sağa doğru yaz
        if ust <= alt:
            for i in range(sag, sol-1, -1):
                matris[alt][i] = sayi
                sayi += 1
            alt -= 1

        # Sol sütunu yukarıya doğru yaz
        if sol <= sag:
            for i in range(alt, ust-1, -1):
                matris[i][sol] = sayi
                sayi += 1
            sol += 1

    # Matrisi şekilli yazdır
    for satir in matris:
        for eleman in satir:
            print(f"{eleman:3}", end=" ")
        print()

# Kullanıcıdan giriş alarak spiral oluştur
boyut = int(input("Spiral boyutunu gir (örn. 5): "))
spiral_deseni_olustur(boyut)

