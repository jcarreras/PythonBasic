def sumal(llista):
    ls=[]
    for e in llista:
        ls.append(e*10)
    return ls


#Programa principal
l = [2, 3, 4]
print(l)
s=sumal(l)
print("La llista original és {} i la modificada és {}".format(l,s))