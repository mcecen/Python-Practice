# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:18:07 2023

@author: MUSTAFA
"""
#%%Example-1 --> Kaçı dizili cümle yazdırma

print("Twinkle, twinkle, little star,\n","\t\tHow I wonder what you are!\n","\t\t\tUp above the world so high,\n","\t\t\tLike a diamond in the sky.\n","Twinkle, twinkle, little star,\n","\t\tHow I wonder what you are") 
     
#%%Example-2 --> Daire Alanı Hesaplama

yaricap = int(input("Yarıçap Değeri Giriniz: "))
pi = 3.14
alan = pi*yaricap*yaricap
print("Dairenin Alanı:" , alan)

#%%Example-3 --> Kullanıcıdan Alınan Ad ve soyadı ters yazdırma

firstName = input("Adınızı Giriniz: ")
lastName = input("Soyadınızı Giriniz: ")

print("Merhaba, " + lastName + " " + firstName)

#%%Example-4 --> Verilen renk listesindeki ilk ve son renkleri gösterme

color_list = ["Kırmızı","Yeşil","Beyaz","Siyah"]

print("Listedeki İlk Renk:", color_list[0])
print("Listedeki Son Renk:", color_list[len(color_list)-1])

#%%Example-5 --> Format Kullanımı

exam_st_date = (30, 7, 2023)
print("Sınavın Tarihi: {}/{}/{}".format(exam_st_date[0],exam_st_date[1],exam_st_date[2]))

#%%Example-6 --> Bir tamsayıyı (n) kabul eden ve n+nn+nnn değerini hesaplayan bir Python programı yazın.

n = int(input("n değerini giriniz : "))
n1 = int( "{}".format(n))
n2 = int( "{}{}".format(n,n))
n3 = int( "{}{}{}".format(n,n,n))
print (n1+n2+n3)

#%%Example-7 --> Tek mi Çift mi

number = input("Sayı Giriniz: ")

try:
    if int(number)%2 == 0:
        print("Girilen sayı çifttir")
    
    elif int(number)%2 == 1:
        print("Girilen sayı tektir")
        
    else:
        print("Geçerli değer giriniz!!")
        
except:
    print("Veri hatası")
    
finally:
    print("İşlemler bitti...")
    
#%%Example-8 --> Dizideki 5 sayısını sayma

dizi = [1,2,3,4,5,6,7,8,9,5,5,"a",2.1,5,"mustafa",[3,3,5]]

sayac = 0
for i in dizi:
    if i ==5:
        sayac+=1
        
print("Dizide geçen 5 sayısı:", sayac)

#%%Example-9 --> Belirli bir dizenin ilk 2 karakterinin n (negatif olmayan tamsayı) kopyalarını almak için bir Python programı yazın. Uzunluk 2'den azsa tüm dizenin n kopyasını döndürün.

def substring_copy(text, n):
  sinirDeger = 2
  
  if sinirDeger > len(text):
    sinirDeger = len(text)
    
  substr = text[:sinirDeger]
  result = ""
  
  for i in range(n):
    result = result + substr
  return result

print(substring_copy('abcdef', 2))
print(substring_copy('p', 3)); 

#%%Example-10 --> Geçirilen bir harfin sesli harf olup olmadığını test etmek için bir Python programı yazın.

def sesliSessiz(harf):
    sesli_harfler = "aeıioöuü"
    return harf in sesli_harfler

sesliSessiz("p")

#%%Example-11 --> Belirli bir değerin bir değer grubu içinde yer alıp almadığını kontrol eden bir Python programı yazın..

def degerVarmi(veri,aranacak):
    
    for i in veri:
        if aranacak == i:
            return True
    return False

degerVarmi([1,2,3,4,5,6,7], 2)

#%%Example-12 --> Belirli bir sayı listesindeki tüm çift sayıları aynı sırayla yazdırmak için bir Python programı yazın ve dizide 237'den sonra yazdırmayı bırakın.

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527]

for i in numbers:
    
    if i ==237:
        print(i)
        break
    
    elif i%2 == 0:
        print(i)
        
#%%Example-13 --> İki listedekiş ortak renleri yazdıran bir Python programı yazın.

color_list_1 = set(["Beyaz", "Siyah", "Kırmızı"]) 
color_list_2 = set(["Kırmızı", "Yeşil"])

ortak_renkler = []

for i in color_list_1:
    for j in color_list_2:
        if i == j:
            ortak_renkler.append(i)
print(ortak_renkler)

#%%Example-14 --> Dört basamaklı sayının rakamlarını toplama

sayi = int(input("Dört basamaklı sayı giriniz:"))

binler = sayi//1000
print("Sayının binler basamağı:",binler)

yuzler = (sayi - binler*1000)//100
print("Sayının yüzler basamağı:",yuzler)

onlar = (sayi - binler*1000 - yuzler*100)//10
print("Sayının onlar basamağı:",onlar)

birler = (sayi - binler*1000 - yuzler*100 - onlar*10)
print("Sayının birler basamağı:",birler)

print("Sayının rakamları toplamı:", birler+onlar+yuzler+binler)

#%%Example-15 --> Çarpım Tablosu

for i in range(1,10):
    print("{}'li Çarpım:\n".format(i))
    print("****************\n")

    for j in range(1,10):
        print("{} x {} = {}\n".format(i,j,i*j))
        
#%%Example-16 --> Klavyeden girilen 10 adet sayıyı toplama

toplam = 0

for i in range(1,11):
    
    sayi = int(input("{}. sayıyı giriniz:".format(i)))
    toplam = toplam + sayi
    
print("Girilen 10 tane sayının toplamı: ", toplam)


#%%Example-17 --> Çokgen Alan ve Çevre Hesabı  
       
def kareCevreAlan(self,kenar):
        kareCevre = 4 * kenar
        kareAlan = kenar * kenar
        print("Karenin Çevresi:{}, Karenin Alanı:{}".format(kareCevre, kareAlan))
    
def dikdortgenCevreAlan(self,kısa_kenar, uzun_kenar):
        dıkdortgenCevre = 2*(kısa_kenar + uzun_kenar)
        dıkdortgenAlan = (kısa_kenar * uzun_kenar)
        print("Dikdörgenin Çevresi:{}, Dikdörtgenin Alanı:{}".format(dıkdortgenCevre, dıkdortgenAlan))

def ucgenAlan(self,taban,yukseklik):
        uAlan=(taban * yukseklik)/2
        print("Üçgenin Alanı:{}".format(uAlan))

def daireCevreAlan(self,yaricap):
        pi = 3.14
        daireCevre = 2 * pi * yaricap
        daireAlan = pi * yaricap * yaricap 
        print("Dairenin Çevresi:{}, Dairenin Alanı:{}".format(daireCevre, daireAlan))
    
kareCevreAlan(5)
dikdortgenCevreAlan(10,11)
ucgenAlan(7,8)
daireCevreAlan(9)

kareKenar = int(input("\nKarenin kenar uzunluğunu giriniz: "))
dıkdortgenKısaKenar = int(input("Dikdörtgenin kısa kenar uzunluğunu giriniz: "))
dıkdortgenUzunKenar = int(input("Dikdörtgenin uzun kenar uzunluğunu giriniz: "))
ucgenTaban = int(input("Üçgenin taban uzunluğunu giriniz: "))
ucgenYukseklik = int(input("Üçgenin yükseklik uzunluğunu giriniz: "))
daireYaricap = int(input("Dairenin yarıçap uzunluğunu giriniz:"))

kareCevreAlan(kareKenar)
dikdortgenCevreAlan(dıkdortgenKısaKenar,dıkdortgenUzunKenar)
ucgenAlan(ucgenTaban,ucgenYukseklik)
daireCevreAlan(daireYaricap)
    
#%% Example-18 --> Karakter dizi içeriği karşılaştırma

ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

fark =""
for s in ilk_metin:
    if not s in ikinci_metin:
        if not s in fark:
            fark+=s
print(fark)
    
#%% Example-19 --> Metindeki harf sayısı

metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
edilmesi neredeyse bir gelenek halini almıştır."""

harf = input("Sorgulamak istediğiniz harf: ")
sayı = ''
for s in metin:
    if harf == s:
        sayı += harf
print(len(sayı))

#%% Example-20 --> Kullanıcıdan 10 adet sayı alıp ortalamasını veren program

sayılar = 0
notlar = []
for i in range(10):
    veri = int(input("{}. not: ".format(i+1)))
    sayılar += veri
    notlar += [veri]
print("Girdiğiniz notlar: ", *notlar)
print("Not ortalamanız: ", sayılar/10)









