a=int(input("Introduce el primer valor: "))
b=int(input("Introduce el segundo nombre: "))

c= a % b

print("La operación de {} y {} es {}".format(a, b, c))

if c==0:
    print("El resto entre {} y {} es par, o sea 0".format(a, b))

elif c!=0:
    print("El resto entre{} y {} es Impar".format(a, b))

#Cambio
a=int(input("Introduce el primer valor: "))
b=int(input("Introduce el segundo nombre: "))

if a>=b:
    print("{} es mayor o igual que {}".format(a, b))

elif a==b:
    print("{} es igual a {}".format(a, b))

else:
    print("{} no es mayor que {}".format(a, b))

print("La operación de {} y {} es {}".format(a, b, c))