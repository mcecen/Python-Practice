isimler = ["Mustafa", "Ahmet", "Ayşe", "Ali"]
print(isimler)
print(isimler[0])
print(isimler[1])
print(len(isimler)) #length --> uzunluğunu verir.
isimler[0] = "Çabuk Kredi"
print(isimler)
print(isimler[0])
print(type(isimler))
isimler.append("Mehmet")
print(isimler)
isimler.remove("Mehmet")

#list constructor
sehirler = list(("Ankara", "İstanbul", "Ankara"))
print(sehirler)

#DİĞER FONKSİYONLAR

#print(sehirler.clear()) #listeyi temizler
print("Ankara Kelime Sayısı: "+ str(sehirler.count("Ankara"))) #verilen elemandan listede kaç tane olduğunu söyler
print("Ankara İndexi: "+ str(sehirler.index("Ankara"))) #verilen elemanın index numarasını(sırasını söyler). aramada ilk gördüğü elemanın indexini söyler
sehirler.pop(1) #verilen index numarasındaki kaydı siler
sehirler.insert(0, "Tokat") #verilen indexe ilgili veriyi ekler
print(sehirler)
sehirler.reverse() #listeyi tersine çevirir
print(sehirler)

sehirler3=sehirler.copy() #kopyasını oluşturur.
sehirler2 = sehirler #listeler referans tiptir. değişiklikler tümünü etkiler. yani bellekte aynı yeri işaret ederler.
sehirler2[0]="İzmir"
print(sehirler)
print(sehirler2)
print(sehirler3)

sehirler.extend(sehirler3) #listeleri birleştirir.
sehirler.sort() #alfabetik veya sayısal olarak sıralama yapar.
print(sehirler)








