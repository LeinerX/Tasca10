def dectobin(N):
    return bin (N)
def dectooct(N):
    return oct (N)
def dectohex(N):
    return hex (N)

#Programa Principal
x=int(input("Introduce un número en Decimal: "))
print(dectobin(x))
print(dectohex(x))
print(dectooct(x))