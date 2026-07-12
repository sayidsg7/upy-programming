# Ejercicio 16 - Sumar solo los positivos
# Lee varios numeros y suma unicamente los positivos.
# El programa termina cuando el usuario ingresa 0.

suma = 0
print("Ingresa numeros (ingresa 0 para terminar):")

numero = float(input("Numero: "))
while numero != 0:
    if numero > 0:
        suma += numero
    numero = float(input("Numero: "))

print(f"La suma de los numeros positivos es: {suma}")
