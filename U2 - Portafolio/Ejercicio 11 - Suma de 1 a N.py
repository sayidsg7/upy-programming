# Ejercicio 11 - Suma de 1 a N
# Calcula la suma de todos los numeros desde 1 hasta N usando un ciclo.

n = int(input("Ingresa un numero entero positivo N: "))

if n < 1:
    print("N debe ser un entero positivo.")
else:
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"La suma de 1 a {n} es: {suma}")
