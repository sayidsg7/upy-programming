# Ejercicio 3 - Vocal o consonante
# Determina si una letra es vocal o consonante.

letra = input("Ingresa una letra: ").lower()

if len(letra) != 1 or not letra.isalpha():
    print("Entrada invalida. Debes ingresar una sola letra.")
elif letra in "aeiou":
    print(f"La letra '{letra}' es una VOCAL.")
else:
    print(f"La letra '{letra}' es una CONSONANTE.")
