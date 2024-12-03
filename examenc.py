"""
Llegir una cadena de caràcters i substituir les vocals per punts
"""

#Programa principal
s = input("Introdueixi la cadena de caràcters: ")
l = list(s)
r=[]
for e in l:
    if e in "aeiou":
        r.append(".") 
    else:
        r.append(e)
s = " ".join(r)
print(s)