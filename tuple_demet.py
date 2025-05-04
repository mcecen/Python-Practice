#listelere benzerdir. demet olarak da isimlendirilir.
#tek farkı listelerde elemanları değiştirebiliyorken, tupleda değiştirmek söz konusu değildir.
#bu veri yapısı performanslı bir data sağlar.

tupleDemet = (2, 4, 6, "Ankara", (2, 3, 4,), [])
liste = [2, 4, 6, "Ankara", [3, 4, 5], ()]

liste[0] = 1
#tupleDemet[0] = 1 #hata verir. tuple elemanları değiştirilemez

tupleDeger = ("Mustafa",) #tek elemanlı değerlerde sistemin verinin string mi yoksa tuple mı olduğunu anlaması için virgül eklenir.
print(type(tupleDeger))
print(tupleDemet[1:2])
print(liste[1:2])
print(tupleDemet[-2])
print(liste[-2])
print(type(tupleDemet))
print(type(liste))
print(tupleDemet)
print(liste)
print(len(tupleDemet))
print(len(liste))

