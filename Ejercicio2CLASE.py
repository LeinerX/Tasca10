def Ver_si_el_número_es_par_o_impar():
    
def Salida():

def menu_Par_Impar():
    x = 1
    while x>0:
        print("""
            Menú de Par y Impar
              1. Ver si el número es par o impar
              2. Salida
            """)
        x = int(input("Elige la opción: "))
        if x>0 and x<3:
            return x
        else:
            print("Vuelve a Intentarlo: \n")

opcio = 1
while opcio>0:
    opcio = menu_Par_Impar()
    match opcio:
        case 1:
            Ver_si_el_número_es_par_o_impar()
        case 2:
            print("Gràcies, m'en vaig!")
            opcio=-1

n = int(input("Introduce número:"))
if n%2==0:
    print("Es par")
else:
    print("Es Impar")