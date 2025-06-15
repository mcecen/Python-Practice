from collections import Counter

def harf_sayaci():
    metin = input("Bir metin girin: ").lower()
    sayac = Counter(metin)

    print("Harflerin sayısı:")
    for harf, adet in sorted(sayac.items()):
        if harf.isalpha():
            print(f"{harf}: {adet}")

if __name__ == "__main__":
    harf_sayaci()