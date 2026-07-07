# Problema 11: Suma de 1 + 2 + ... + N usando while

n = int(input("Ingresa un entero positivo N: "))

suma = 0       # inicializa
i = 1          # inicializa contador

while i <= n:  # condicion
    suma = suma + i
    i = i + 1  # actualiza

print("La suma de 1 +", "2 + ... +", n, "es:", suma)
