#Fer el factorial de forma iterativa
n = int(input("Introdueixi el número a fer el factorial: "))
r=1
while(n>0):
    r=r*n
    n=n-1
print(r)  


#Fer el factorial en recursivitat
def fact(n):
    if n<=0:
        return 1
    else:
        return n * fact(n-1)
print(fact(3))
