liste = ["Kabak","Kaban","Kabin","Kabar","Kabuk","Kabul","Kacan","Kacar"
         ,"Kacik","Kacis","Kadar","Kapan","Kadem","Kalan","Kader","Kagan","Taban"]
farkli = []

def farkliBul(kelime):
    for i in liste:
        j = 0
        benzerlik = 0
        
        while j < len(i):
            if kelime[j] == i[j]:
                benzerlik += 1
            j = j + 1
            
        if benzerlik == len(kelime) - 1:
           farkli.append(i)
           
    print kelime + " kelimesinden 1 harf farkli kelimeler : \n",farkli 


farkliBul("Kaban")
