# Ejercicio 2 - Valor dentro de un rango
# Verifica si un numero se encuentra dentro de un rango dado.

limite_inferior = float(input("Ingresa el limite inferior del rango: "))
limite_superior = float(input("Ingresa el limite superior del rango: "))
valor = float(input("Ingresa el valor a verificar: "))

if limite_inferior <= valor <= limite_superior:
    print(f"El valor {valor} SI esta dentro del rango [{limite_inferior}, {limite_superior}].")
else:
    print(f"El valor {valor} NO esta dentro del rango [{limite_inferior}, {limite_superior}].")
