a = int(input("Escriu un número: "))
b = int(input("Escriu un número: "))
c = int(input("Escriu un número: "))
if a > b:
    if b > c:
        print("{} és major que {} i aquest és major que {}".format(a, b, c))
    elif b<c:
        if a>c:
            print("{} és major que {} i aquest és major que {}".format(a, c, b))
        elif c>a:
            print("{} és major que {} i aquest és major que {}".format(c, a, b))
        else:
            print("{} i {} són iguals i majors que {}".format(a,c,b))
    else:
        print("{} i {} són iguals i menors que {}".format(b,c,a))
elif a < b:
    E