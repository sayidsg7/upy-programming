# Ejercicio 17 - Triangulo de asteriscos
# Imprime un triangulo de asteriscos con la altura indicada por el usuario.

altura = int(input("Ingresa la altura del triangulo: "))

if altura < 1:
    print("La altura debe ser un entero positivo.")
else:
    for fila in range(1, altura + 1):
        print("*" * fila)
