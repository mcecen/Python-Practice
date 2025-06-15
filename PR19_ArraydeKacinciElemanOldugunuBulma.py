"""
Aranan değerin Array içerisinde kaçıncı eleman olduğunu bulan Java Kodu yazınız.

    Array: [12,15,43,23,56,76,78,90,77,43]

    Aranan değer:56

    Beklenen Çıktı:
    56 sayısı arrayin 4. elemanı
"""
liste = [12,15,43,23,56,76,78,90,77,43]
sayi = int(input("Aranacak sayiyi giriniz: "))

for i in range(len(liste)-1):
    if(liste[i]==sayi):
        print("Aranan sayi",i+1,"inci elemandır.")