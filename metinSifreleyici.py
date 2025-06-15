def sezar_sifreleme(metin, kaydirma):
    sifreli = ""
    for char in metin:
        if char.isalpha():
            ascii_bas = 65 if char.isupper() else 97
            sifreli += chr((ord(char) - ascii_bas + kaydirma) % 26 + ascii_bas)
        else:
            sifreli += char
    return sifreli

def main():
    metin = input("Şifrelenecek metni girin: ")
    while True:
        try:
            kaydirma = int(input("Kaydırma miktarını girin (örneğin 3): "))
            break
        except ValueError:
            print("Lütfen sayı girin.")
    sonuc = sezar_sifreleme(metin, kaydirma)
    print(f"Şifreli metin: {sonuc}")

if __name__ == "__main__":
    main()