# Problema 10: Positivo par, positivo impar o no positivo

numero = int(input("Ingresa un numero: "))

if numero > 0:
    if numero % 2 == 0:
        print("Positivo par")
    else:
        print("Positivo impar")
else:
    print("No es positivo")
