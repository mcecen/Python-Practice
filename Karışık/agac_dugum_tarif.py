#Verilen Agac ornegine "Ozel" bir cozumdur, Genel bir cozum degildir.

agac = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]

def arama(harf):
    s1 = ""
    s2 = ""
    for i in agac:
        for j in i:
            for k in j:
                if k == harf:
                    x = agac.index(i) 
                    y = i.index(j)
                    z = j.index(k)
                    

    if x == 1:
        s1 = "sol"
    elif x == 2:
        s1 = "sag"

    if y == 1:
        s2 = "sol"
    elif y == 2:
        s2 = "sag"

    print agac[x][y][z] + "'nin konumu, Agacin " + s1 + " alt agacinin " + s2 + " dugumudur"
    
arama('d')
arama('e')
arama('f')
