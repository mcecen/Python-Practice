"""
String array dizisindeli 4 harfli kelimeleri return eden methodu yazınız.


    Test Data:
    isFourLetters(["Tomato", "Potato", "Pair"])

     ["Pair"]
"""
dizi = ["Tomato", "Potato", "Pair"]
dort_harf_dizi = []

def isFourLetters(arr):
    for kelime in arr:
        if len(kelime) == 4:
            dort_harf_dizi.append(kelime)
    print(dort_harf_dizi)

isFourLetters(dizi)