# -*- coding: utf-8 -*-
#r --> read, a --> append, w -- > write, x --> create

#%%Dosyaya yazma

isim = open("isim.txt", "w")
isim.write("Mustafa ÇEÇEN"),
isim.close()

#%%Dosya okuma

fihrist = open("fihrist.txt", "r") #ya da fihrist = open("fihrist.txt")
print(fihrist.read())
print(type(fihrist.read()))

print(fihrist.readline())
print(type(fihrist.readline()))

print(fihrist.readlines())
print(type(fihrist.readlines()))

#%%
with open("fihrist.txt", "a") as f:
    f.write("\nSelin Özden\t: 0212 222 22 22")
    
f = open("fihrist.txt", "r+")
f.truncate(1024*3)
f.close()

f = open("fihrist.txt")
f.read()















