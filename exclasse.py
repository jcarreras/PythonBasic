a="Hola"
b=input("Llegir paraula: ")
# Mostri caracters de la paraula llegida
for e in b:
    print(e)
# Longitud paraula
print(len(b))

# Comparar-les
if a == b:
    print("{} i {} són iguals ".format(a, b))
else:
    print("{} i {} són diferents ".format(a, b))

# Ajuntar-les amb un guió
print(a+"-"+b)

# Repetir-la 3 vegades
print(b*3)

# Mirar si la vocal a és dins b(string)
if "a" in b:
    print("a és dins l'string {}".format(b))
else:
    print("a no hi és")
    
