# Listelere benzerdir
# En önemli özelliği indexsiz ve sırası elemanlardan oluşmasıdır.
# Veri tekrarı söz konusu değildir. Tüm elemanlar eşsizdir.(unique)
# Bu veri yapısı performanslı bir data sağlar.
# Elemanlarında değişiklik yapılamaz

studentSet = {"Mustafa", "Ayşenur", "Burak"}
studentSet2 = set("a", "b", "c")
print(studentSet)

for student in studentSet:
    print(student)

print("Derin" in studentSet) #büyük küçük harf duyarlılığı vardır.

if "Derin" in studentSet:
    print("Listede var")

studentSet.add("Ali") #kümeye eleman ekler
print(studentSet)

studentSet.update(["Ahmet", "Mehmet"])
print(studentSet)
print(len(studentSet))

studentSet.remove("Ali") #verilen elemanı siler. bulamazsa hata döner.
print(studentSet)
print(len(studentSet))

studentSet.discard("Ali") #verilen elemanı siler. bulamazsa işlem yapmaz ,hata dönmez.
print(studentSet)
print(len(studentSet))

x= studentSet.pop() #en son elemanı siler. sıralı olmadığı için herhangi bir değer olabilir.
print(studentSet)
print(len(studentSet))

studentSet.clear() #kümenin içeriğini siler. boş küme döner.
print(studentSet)
print(len(studentSet))

del studentSet #kümeyi tamamen siler.
print(studentSet)

#UNION İŞLEMİ --> kümeleri birleştirir, ortak elemanları 1 kere yazar.

setA = {1, 2, 3, 4, 5}
setB = {1, 3, 4, 6, 7, 8}

print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))


#INTERSECTION İŞLEMİ --> kümelerin kesişimini verir.

print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))

#DIFFERENCE İŞLEMİ --> kümelerin farkını verir.

print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

#SYMETRIC DIFFERENCE İŞLEMİ --> kümelerin farkını verir.

print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))


