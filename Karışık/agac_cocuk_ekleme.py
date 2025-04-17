#Verilen Agac ornegine "Ozel" bir cozumdur, Genel bir cozum degildir.

agac = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]

def ekle(harf):
    for i in agac:
        for j in i:
            if len(j) != 3 and type (j) != type ('u'):
                j.append(harf)
                j.append([])
                j.append([])
    print agac

ekle('g')
