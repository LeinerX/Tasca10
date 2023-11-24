#Variables Compuestas(suma(solo se puede sumar("+="))).
"""a=[2, 3, 4]
b=[2, 5, 6, 10]
a += b #Esto es igual a "a=a+b"
print(a)"""

#Esto es la suma de Variables Simples(En este sí se puede *, /, +, -).
"""a=int(input("Introduce el primer valor: "))
b=int(input("Introduce el segundo valor: "))
a *= b"""

#Se remplaza la a[2]=9, y luego se imprime.
"""a = [2, 3, 4]
b = [20, 30, 40]

a = b
print(a)
a[2]=9
print(b)"""

#Se le otorga valor a "a" y luego se lo reasigna a "b", éste no cambia a 15, se queda en el valor dado.
"""a = int(input("Number: "))
b = int(input("Number: "))
a = b
print(a)
a = 15
print (b)
print(a)"""

#Se le agrega(append) un valor la lista (a), el usuario agrega.
"""a=[1, 2, 3, 4, 5, 6, 7, 8]
z=int(input("Introduce el tamaño de la lista: "))

for x in range(z):
    a.append(input("Introduce un número: "))
print(a)

#Programa Principal
a = leer_lista()
b = leer_lista()
c = []
for i in range(len(5)):
    c.append(a[i]*[i])
print("La multiplicación de la lista {} para la lista {} es {}".format(a, b, c))"""

#is o ==
"""a = [2, 3, 4]
b = [2, 3, 4]
if b ==/is a:
    print("Apuntan al mismo lugar")
else:
    print("No apuntan al mismo lugar")"""

#
"""a = [3, (1,3), [4, 5, 6], 7, "hola", '0',0,1]

if a == 'b':
        print("a es b")
elif  a == 'c':
        print("a es c")
elif a == 'd':
    print("a es d")
elif a == 'e':
    print("a es e")
else:
    print("No vale nada")"""

"""
a = [3, (1,3), [4, 5, 6], 7, "hola", '0',0,1]
match a:
    case 'b':
        print("a es b")
    case 'c':
        print("a es c")
    case 'd':
        print("a es d")
    case 'e':
        print("a es e")
"""

"""
#Hexadecimal a Binario, octal y Decimal
def hextonum(hex):
    pnum = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10
        }
    if hex in pnum:
        return pnum[hex]
    else:
        return int (hex)
def hextodec2(hex):
    hex = hex.lower()
    hex = hex[::-1]
    decimal = 0
    posición = 0
    for digit in hex:
        valor = hextonum(digit)
        elevado = 16 ** posición
        pnum = elevado * valor
        decimal += pnum
        posición += 1
    return decimal
def hextobin(número):
    a=int(número,16)
    return dectobin(a)

def hextooct(número):
    a=int(número,16)
    return dectooct(a)

def hextodec(número):
    a=int(hextodec2)(número)
    return a
"""