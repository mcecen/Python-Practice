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
        self.onceki = None
        self.adim = 0
    def renkKaydet(self, renk):
        self.renk = renk
    def adimKaydet(self, adim):
        self.adim = adim
    def oncekiKaydet(self, onceki):
        self.onceki = onceki
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
    s.oncekiKaydet(None)
    s.renkKaydet('gri')
    Q = Queue()
    Q.enqueue(s)
    while (Q.size() > 0):
        w = Q.dequeue()
        if w.ad == son:
            break
        else:
            for v in w.komsuAl():
                if (v.renkAl() == 'beyaz'):
                    v.renkKaydet('gri')
                    v.adimKaydet( w.adimAl() + 1 )
                    v.oncekiKaydet(w)
                    Q.enqueue(v)
        
            w.renkKaydet('siyah')
         
    sonuc = son
    adim = graf.vertexAl(son).adim
    i = graf.vertexAl(baslangic)
    j = graf.vertexAl(son)

    while i.ad != j.ad:
        j = graf.vertexAl(j.onceki.ad)
        sonuc = j.ad + " -> " + sonuc
        
    print "Sonuc =",sonuc
    print "Adim sayisi =",adim

    
kelimeler = ["fool","foul","foil","fail","fall","pall","poll","pool","cool","pole","pope","pale","sale","page","sage"]
graf = grafCiz(kelimeler)
bfs(graf,"fool","sage")
