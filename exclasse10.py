

"""
#Exercici 6
p=""
l=[]
while (p!="."):
    p = input("Introdueixi una frase: ")
    if p!=".":
        s = p.lower()
        p = s.title()
        l.append(p)
print("Les frases introduïdes són: {}".format(l))
print("Ja hem acabat!") 


#Exercici 5
p=""
l=[]
while (p!="%"):
    p = input("Introdueixi una paraula: ")
    if p!="%":
        l.append(p.title())
print("Les paraules introduïdes són: {}".format(l))
print("Ja hem acabat!")
#Exercici 4
p=""
l=[]
while (p!="/"):
    p = input("Introdueixi una paraula: ")
    if p!="/":
        l.append(p.upper())
print("Les paraules introduïdes són: {}".format(l))
print("Ja hem acabat!")

#Exercici 3
p=""
l=[]
while (p!="?"):
    p = input("Introdueixi una paraula: ")
    if p!="?":
        l.append(p.lower())
print("Les paraules introduïdes són: {}".format(l))
print("Ja hem acabat!")

#Exercici 2
p=""
l=[]
while (p!=":"):
    p = input("Introdueixi una paraula: ")
    if p!=":" and p[0]=="A":
        l.append(p)
    if len(l)==4:
        p="."
print("Les paraules són: {}".format(l))
print("Ja hem acabat!")


#Exercici 1
p=""
l=[]
while (p!="."):
    p = input("Introdueixi una paraula: ")
    if p!="." and len(p)==4:
        l.append(p)
    if len(l)==4:
        p="."
print("Les paraules són: {}".format(l))
print("Ja hem acabat!")
"""