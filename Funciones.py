#Intercambio de Valores
"""def intercambio(a,b):
    return b,a

x="a"
y="b"
print("El valor de x es {} y el de y es {}".format(x,y))
x,y = intercambio(x,y)
print("Después de el intercambio, el valor de x es {} y el de y es {}".format(x,y))"""

def mayor(x,y):
    if x>y:
        return x
    else:
        return y

x = int(input("Introduce el 1er número: "))
y = int(input("Introduce el 2do número: "))
z = mayor(x,y)
print("El mayor entre {} y {} es {}".format(x,y,z))