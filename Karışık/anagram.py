kelime1 = raw_input("1. kelimeyi giriniz : ")
kelime2 = raw_input("2. kelimeyi giriniz : ")

liste1 = []
liste2 = []
j = 0
anagram = True

for i in kelime1:
    if (kelime1.count(i) * i) not in liste1:
        liste1.append(kelime1.count(i) * i)

for i in kelime2:
    if (kelime2.count(i) * i) not in liste2:
        liste2.append(kelime2.count(i) * i)


while anagram and j < len(liste1):
    if liste1[j] not in liste2:
        anagram = False
    j = j + 1

print "\nAnagram" if anagram else "\nAnagram Degil"
