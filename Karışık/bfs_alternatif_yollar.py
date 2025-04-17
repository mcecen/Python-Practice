class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
class Vertex:
    def __init__(self,num):
        self.ad = num
        self.komsular = []
        self.renk = 'beyaz'
        self.onceki = [] # Farkli yollar icin turu liste oldu.
        self.adim = 0
        self.max = 1 # En fazla kac yol oldugunu tutar.
    def renkKaydet(self, renk):
        self.renk = renk
    def adimKaydet(self, adim):
        self.adim = adim
    def oncekiKaydet(self, onceki):
        self.onceki.append(onceki) # Liste oldugu icin yolu, listenin sonuna ekledik
    def komsuKaydet(self,komsu):
        self.komsular.append(komsu)
    def renkAl(self):
        return self.renk
    def adimAl(self):
        return self.adim
    def oncekiAl(self):
        return self.onceki
    def komsuAl(self):
        return self.komsular
class Graf:
    def __init__(self):
        self.vertListe = {}
        self.vertSayi = 0
        
    def vertexEkle(self,key):
        self.vertSayi = self.vertSayi + 1
        yeniVertex = Vertex(key)
        self.vertListe[key] = yeniVertex
        return yeniVertex
        
    def vertexAl(self,n):
        if self.vertListe.has_key(n):
            return self.vertListe[n]
        else:
            return None
    def has_key(self,sayi):
        return self.vertListe.hash_key(n)

    def kenarEkle(self,f,t):
        if not self.vertListe.has_key(f):
            nv = self.vertexEkle(f)
        if not self.vertListe.has_key(t):
            nv = self.vertexEkle(t)
        self.vertListe[f].komsuKaydet(self.vertListe[t])
    def __iter__(self):
        return self.vertListe.itervalues()
def grafCiz(kelimeler):
    d = {}
    g = Graf()
    for kelime in kelimeler:
        for i in range(5):
            bucket = kelime[0:i] + '_' + kelime[i+1:5]
            if d.has_key(bucket):
                d[bucket].append(kelime)
            else:
                d[bucket] = [kelime]

    for i in d.keys():
        for j in d[i]:
            for k in d[i]:
                if j != k:
                    g.kenarEkle(j,k)
    return g

def bfs(graf,baslangic,son):
    s = graf.vertexAl(baslangic)
    s.adimKaydet(0)
    s.oncekiKaydet('None')
    s.renkKaydet('gri')
    Q = Queue()
    Q.enqueue(s)
    while (Q.size() > 0):
        w = Q.dequeue()
        
        for v in w.komsuAl():
            v.max = w.max # v'ye gelme kombinasyon sayisi, w'ye gelmeye esit
            if (v.renkAl() == 'beyaz'):
                v.renkKaydet('gri')
                v.adimKaydet( w.adimAl() + 1 )
                v.oncekiKaydet(w.ad)
                Q.enqueue(v)
            elif (v.renkAl() == 'gri' and v.adim == w.adim + 1):
                v.oncekiKaydet(w.ad)
                
            v.max *= len(v.onceki) # v'ye gelmek icin yol sayisini guncelle
            
        w.renkKaydet('siyah')
    return graf


# Fonsiyonun calisma mantigi : Oncelikle olabilecek tum kombinasyon sayisi bulunur.
# Daha sonra baslangic dugumden son dugume kadar "en kisa yol" tarifine uyan tum 
# dugumlerin "onceki" listesi, kombinasyon sayisi kadar genisletilir.
# Ornegin: "sage" dugumunun "onceki" listesi ['sale','page'] ve Kombinasyon
# sayimiz da 4 olsun. Biz bu listeyi ['sale','page','sale','page'] olarak genisletiriz.
# Bu islemi "en kisa yol" tarifine uyan tum dugumlerde yaparsak, ekrana yazdirirken
# cok buyuk bir kolaylik saglar. Ornegin: 6 adimlik bir cozum yolumuz olsun. Biz
# dugumlerin "onceki" lerini listeledik. Artik tersten giderek tum dugumlerin 0. indisi
# 1.Cozum, 1. indisi 2. Cozum.. seklinde ilerler. 

def alternatif_yol(graf,baslangic,son):
    
    i = graf.vertexAl(baslangic)
    j = graf.vertexAl(son)
    maximum = j.max
    degisim = 0
    j.onceki += j.onceki[::-1]

    while i.ad != j.ad: # En kisa yolu bulmak icin
        kombinasyon_sayisi = len(j.onceki) # Farkli yollarin listelerini genisletmek icin
        
        for x in range(kombinasyon_sayisi):
            k = graf.vertexAl(j.onceki[x])
            if degisim % 2 == 0:
                k.onceki += k.onceki[::-1]
            else:
                k.onceki *= (maximum / len(k.onceki))

        degisim += 1
        j = graf.vertexAl(j.onceki[0]) # Islemi biten dugumun en kisa yol icin ilerlemesi

    j = j = graf.vertexAl(son) # Genisletme islemi tamamlandi.

    print "Alternatif Yollar\n"
    for x in range(j.max):
        sonuc = son # Hedef dugumden baslangic dugumune dogru en kisa yol

        for y in range(j.adim):
            sonuc = j.onceki[x] + " -> " + sonuc            
            j = graf.vertexAl(j.onceki[x]) # 0. indisler 1. Cozum vb.
            
        j = j = graf.vertexAl(son) # 1. Cozumden 2. Cozume gecmek icin Basa donme hareketi
        print sonuc

    

kelimeler = ["fool","foul","foil","fail","fall","pall","poll","pool","cool","pole","pope","pale","sale","page","sage"]
graf = grafCiz(kelimeler)
bfs_sonuc = bfs(graf,"fool","sage")
alternatif_yol(bfs_sonuc,"fool","sage")
