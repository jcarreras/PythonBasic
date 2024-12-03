#Donada una llista que ens retorni que siguin parells
l=[3, 5, 6, 8, 9, 11, 12]

#Versió iterativa
r=[]
for e in l:
    if e%2==0:
        r.append(e)
print(r)

#Versió amb filter(programació funcional)
def parell(x):
    if x%2==0:
        return True
    return False
w=list(filter(parell,l))
print(w)

#Versió amb funció anònima
s=list(filter(lambda x:x%2==0,l))
print(s)
