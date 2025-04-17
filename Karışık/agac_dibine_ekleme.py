class IkilAgac:
    
    def __init__(self, kokObj):
        self.anahtar = kokObj
        self.sol = None
        self.sag = None

    def solaEkle(self, yeniDugum):
        if self.sol == None:
            self.sol = IkilAgac(yeniDugum)
        else:
            a = IkilAgac(yeniDugum)
            a.sol = self.sol
            self.sol = a
            
    def sagaEkle(self, yeniDugum):
        if self.sag == None:
            self.sag = IkilAgac(yeniDugum)
        else:
            a = IkilAgac(yeniDugum)
            a.sag = self.sag
            self.sag = a
            
    def kokDegerAl(self):
        return self.anahtar
    
    def kokDegerVer(self, yeniDeger):
        self.anahtar = yeniDeger
        
    def solCocukAl(self):
        return self.sol

    def sagCocukAl(self):
        return self.sag


def appendLeft(agac,deger):
    if agac.sol != None:
        appendLeft(agac.sol,deger)
    else:
        print "Agacin sol dip dugumu :",agac.kokDegerAl()
        agac.solaEkle(deger)
        print "'" + agac.sol.kokDegerAl() + "'" + " sol dibin soluna eklendi."

def appendRight(agac,deger):
    if agac.sag != None:
        appendRight(agac.sag,deger)
    else:
        print "Agacin sag dip dugumu :",agac.kokDegerAl()
        agac.sagaEkle(deger)
        print "'" + agac.sag.kokDegerAl() + "'" + " sag dibin sagina eklendi."

a = IkilAgac('a')
a.solaEkle('b')
a.sol.solaEkle('d')
a.sol.sagaEkle('e')
a.sagaEkle('c')
a.sag.solaEkle('f')

appendLeft(a,'u')
appendRight(a,'t')
