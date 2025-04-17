# aynen kümeler gibi sırası veri tutar
# günlük hayattaki sözlük gibi düşünülebilir. -- anahtar değer ilişkisi

sozluk = {
    "book" : "kitap",
    "table" : "masa"
}

print(sozluk)
print(sozluk["book"])
sozluk["book"] = "kitap 1"
sozluk["bookk"] = "kitap 1" #eğer içeride anahtar-değer yoksa ekleme yapar
print(sozluk)

sozluk2 = dict(kitap="book", masa="table")
print(sozluk2)
del(sozluk["book"])
print(len(sozluk))