# Ejercicio 13 - Suma de numeros pares
# Calcula la suma de todos los numeros pares desde 1 hasta N.

n = int(input("Ingresa un numero entero positivo N: "))

if n < 1:
    print("N debe ser un entero positivo.")
else:
    suma = 0
    for i in range(2, n + 1, 2):
        suma += i
    print(f"La suma de los numeros pares de 1 a {n} es: {suma}")
