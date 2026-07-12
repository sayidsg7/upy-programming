# Ejercicio 15 - Primer multiplo de 7
# Encuentra el primer multiplo de 7 mayor o igual a un numero dado,
# usando un ciclo while.

n = int(input("Ingresa un numero entero positivo: "))

numero = n
while numero % 7 != 0:
    numero += 1

print(f"El primer multiplo de 7 mayor o igual a {n} es: {numero}")
