def llista_nombres():
    l=[]
    a="1"
    while a!=".":
        a = input("Introdueixi un número: ")
        if a!=".":
            l.append(int(a))
        else:
            print("Adéu!")
    return l

def sumar_llista(ramis):
    suma=0
    for e in ramis:
        suma = suma + e
    return suma

#Programa principal
p = llista_nombres()
print(p)
suma = sumar_llista(p)
print(suma)
print(p[::-1])
print(p)
print(p[-2:])+

