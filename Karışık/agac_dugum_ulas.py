#Verilen Agac ornegine "Ozel" bir cozumdur, Genel bir cozum degildir.

agac = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]

def arama(harf):
    for i in agac:
        for j in i:
            for k in j:
                if k == harf:
                    x = agac.index(i) 
                    y = i.index(j)
                    z = j.index(k)
                    
    print "Aranan "+ harf + "'ye ulasmak icin : agac[" + str(x) + "][" + str(y) + "][" + str(z) + "]"
arama('d')
arama('e')
arama('f')
