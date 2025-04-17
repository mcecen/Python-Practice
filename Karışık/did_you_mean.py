# Minimum edit distance yontemiyle yapilmistir.
import operator

def didYouMean(kelime1, kelime2):
    len1 = len(kelime1)
    len2 = len(kelime2)
    
    matris =[ [0] * (len2 + 1) for i in range(len1 + 1) ] 

    for i in range(0, len1 + 1):
        matris[i][0] = i
        
    for j in range(0, len2 + 1):
        matris[0][j] = j

    for i in range(0, len1 + 1):
        for j in range(0, len2 + 1):
            if kelime1[i-1] == kelime2[j-1]:
                matris[i][j] = matris[i-1][j-1]
            else:
                matris[i][j] = min(matris[i][j-1], matris[i-1][j], matris[i-1][j-1]) + 1
    return matris[i][j] # Yontemin ciktisi : Bir kelimeyi digerine benzetmek icin gereken minimum adim sayisidir.

kelimeler = ["kibrit","egzoz","sarj","surpriz","sarimsak","yalniz"]
kelime = "kbrtii"
hash_depo = {} # Girilen kelimenin diger kelimelerle olan benzerligini tutmak icin depo

for i in kelimeler:
    hash_depo[i] = didYouMean(i,kelime) # Depo edildi

    
sirali_hash = sorted(hash_depo.items(), key = operator.itemgetter(1)) # Depodaki degerlere (value) gore siralandi.

print "--> " + kelime
print "Did you mean " + sirali_hash[0][0] + " ?" # Siralandiktan sonra ilk eleman "en benzer" olandir.
