# Ejercicio 10 - Positivo par o impar
# Determina si un numero es positivo, negativo o cero,
# y si es positivo, indica si es par o impar.

numero = int(input("Ingresa un numero entero: "))

if numero > 0:
    if numero % 2 == 0:
        print(f"El numero {numero} es POSITIVO y PAR.")
    else:
        print(f"El numero {numero} es POSITIVO e IMPAR.")
elif numero < 0:
    print(f"El numero {numero} es NEGATIVO.")
else:
    print("El numero es CERO.")
