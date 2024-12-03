def llegir_llista():
    l=[]
    a="1"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
        else:
            print("Adéu!")
    return l
def lector_de_caracteres(lista):
    xm={}
    for i in lista:
        if i in lista:
            xm[i]=int(1)
        else:
            xm[1] += 1
    print(xm)
 
#Programa principal

l = llegir_llista()
cl = set(l)
if len(l)==len(cl):
    print("No hi ha cap paraula repetida")
else:
    print("N'hi ha de repetides, però encara no sé quines")
