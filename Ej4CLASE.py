#Part 1 of DICK
dick = {"Nombre":"Leiner", "Apellido":"Zapata", "Edad":17}
for element in dick:
    print(element)

#Parte 2 de DICK
dic = {"Nombre":"Leiner", "Apellido":"Zapata", "Edad":17}
for element in dic:
    print("La clave {} tiene el valor {}".format(element, dic[element]))

#Parte 3 of DICK
dic = {"Nombre":"Leiner", "Apellido":"Zapata", "Edad":17}
for x,y in dic.items():
    print("La clave {} tiene el valor {}".format(x,y))

#Parte 4 of DICK
dic.pop(1)
print(dic)

#Parte 5 of DICK
dicB = {"D10S":"MESSI", "Cognome":"Cuccitini", "Años":99}
dic.update(dicB)
print(dicB)