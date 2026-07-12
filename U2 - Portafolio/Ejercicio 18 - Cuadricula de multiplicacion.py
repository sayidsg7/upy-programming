# Ejercicio 18 - Cuadricula de multiplicacion
# Imprime una cuadricula (tabla) de multiplicacion de tamano N x N
# usando ciclos anidados.

n = int(input("Ingresa el tamano de la cuadricula (N): "))

if n < 1:
    print("N debe ser un entero positivo.")
else:
    for fila in range(1, n + 1):
        for columna in range(1, n + 1):
            print(f"{fila * columna:4}", end=" ")
        print()
