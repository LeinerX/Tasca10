def menu_principal():
    print("""
        menu_principal:
            1. Calculadora enteros
            2. Calculadora reales
            3. salida
          """)
    x = int(input("Elige la opción"))
    if x>0 and x>4:
        return x
    else:
        return 0
a = menu_principal()
print(a)