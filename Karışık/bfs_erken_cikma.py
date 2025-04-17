def bfs(graf,baslangic,son): # Baslangic ve Son degerleri iste
    s = graf.vertexAl(baslangic)
    s.adimKaydet(0)
    s.oncekiKaydet(None)
    s.renkKaydet('gri')
    Q = Queue()
    Q.enqueue(s)
    while (Q.size() > 0):
        w = Q.dequeue()
        if w.ad == son: # Kuyruktan cekilen, Hedef dugume ise cik
                break
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

    while i.ad != j.ad: #Tersten gelerek kontrol et
        j = graf.vertexAl(j.onceki.ad) # Tersi guncelle
        sonuc = j.ad + " -> " + sonuc
        
    print "Sonuc =",sonuc
    print "Adim sayisi =",adim
