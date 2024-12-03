def llegir_llista():
    l=[]
    a="1"
    while a!=".":
        a = input("Introdueixi un caràcter diferent a .: ")
        if a!=".":
            l.append(a)
        else:
            print("Adéu!")
    return l

def elements_llista(l):
    d=dict()
    c="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for e in c:
        d[e]=0
    for e in l:
        d[e]+=1
    return d



#Programa principal
p = llegir_llista()
print(p)
d = elements_llista(p)
print(d)
