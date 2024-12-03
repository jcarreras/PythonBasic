#Paràmetres
# String/cadena de caràcters ?? Es passa per valor o per referència
# Després de la prova ens hem adonat que es passa per valor
def modifica_string(s):
    s="Això és un canvi, anem a veure si fora de la funció queda el canvi o no."

s="Bon dia, això és una prova"
print(s)
modifica_string(s)
print(s)


# Per valor, la variable c no es modifica encara que jo la modifiqui dins la funció
def operacio(a, b, c):
    c = a + b
a = 3
b = 4
c = 0
print(c)
operacio(a, b, c)
print(c)


# Per referència, sí modifica el valor
def axllista(l):
    for i in range(len(l)):
        l[i]*=3

# Programa principal
llista=[2, 3, 4]
print(llista)
axllista(llista)
print(llista)