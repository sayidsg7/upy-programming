# Ejercicio 14 - Contar las vocales en una palabra
# Cuenta cuantas vocales tiene una palabra.

palabra = input("Ingresa una palabra: ").lower()

contador = 0
for letra in palabra:
    if letra in "aeiou":
        contador += 1

print(f"La palabra '{palabra}' tiene {contador} vocal(es).")
