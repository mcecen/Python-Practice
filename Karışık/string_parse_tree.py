import operator
class Stack:
 def __init__(self):
     self.items = []

 def isEmpty(self):
     return self.items == []

 def push(self, item):
     self.items.append(item)

 def pop(self):
     return self.items.pop()

 def peek(self):
     return self.items[len(self.items)-1]

 def size(self):
     return len(self.items)
    
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

def ParseTree(string):
    dString = string.split()
    s = Stack()
    Agac = IkilAgac('')
    s.push(Agac)
    simdikiAgac = Agac

    for i in dString:
        if i == '(':
            simdikiAgac.solaEkle('')
            s.push(simdikiAgac)
            simdikiAgac = simdikiAgac.solCocukAl()
        elif i not in '+-*/)':
            simdikiAgac.kokDegerVer(eval(i))
            parent = s.pop()
            simdikiAgac = parent
        elif i in '+-*/':
            simdikiAgac.kokDegerVer(i)
            simdikiAgac.sagaEkle('')
            s.push(simdikiAgac)
            simdikiAgac = simdikiAgac.sagCocukAl()
        elif i == ')':
            Agac = s.pop()
        else:
            print "Verilen string ifadesi duzenli degil."

    return Agac

def hesapla(parseTree):
    operatorler = {'+': operator.__add__ , '-': operator.__sub__ ,
                   '*': operator.__mul__ , '/': operator.__div__}
    solCocuk = parseTree.solCocukAl()
    sagCocuk = parseTree.sagCocukAl()

    if solCocuk and sagCocuk:
        fonk = operatorler[parseTree.kokDegerAl()]
        return fonk(hesapla(solCocuk), hesapla(sagCocuk))
    else:
        return parseTree.kokDegerAl()

print "((4*5)+3) =",hesapla(ParseTree('((4*5)+3)')) #23
print "((9/3)*(2*3)) =",hesapla(ParseTree('((9/3)*(2*3))')) #18
print "(((7-2)/5)+((4*2)*9)) =",hesapla(ParseTree('(((7-2)/5)+((4*2)*9))')) #73
