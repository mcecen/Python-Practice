#Verilen Agac ornegine "Ozel" bir cozumdur, Genel bir cozum degildir.

agac = [3, [9, [2, [], []], [6, [], []]], [4, [23, [], []], []]]

def enb(agac):
        
        x = 0
        y = 0
        z = 0
        enb = 0
        s1 = ""
        s2 = ""
        
        for i in agac:
                if type (i) == type (23) and i > enb:
                        enb = i
                else:
                        for j in i:
                                if type (j) == type (23) and j > enb:
                                        enb = j
                                        x = agac.index(i)
                                        y = i.index(j)
                                
                                elif type (j) == type([]) and len(j) != 0:
                                        for k in j:
                                                if type (k) == type (23) and k > enb:
                                                        enb = k
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
                
        print "Agacin dugumlerinden en buyuk deger :",enb
        print "En buyuk dugumun yeri : Agacin " + s1 + " alt agacinin " + s2 + " dugumudur."
                

enb(agac)
