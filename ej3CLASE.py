def Tercera_Ocurrencia(l,e):
    a = l.count(e)
    if a==0:
        print("No hay ocurrencias en este elemento")
    elif a==1:
        print("La primera ocurrencia del elemento está en la posición {}".format(l.index(e)))
    elif a==2:
        print()
    if a>2:
        print("Hay más de una ocurrencia de {}".format(e))
        p = l.index(e)
        so = l.index(e,(p+1))
        to = l.index(e(so+1))
        print(to)
    else:
        print("Valor no válido")

#Programa Principal
l=(1, 4, 2, (1, 3, 3), 3, 4, 2, 1)
x = int(input("Lea el elemento que quiere buscar la 3ra ocurrencia: "))
Tercera_Ocurrencia(l,x)