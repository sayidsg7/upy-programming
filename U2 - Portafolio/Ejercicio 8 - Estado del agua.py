# Ejercicio 8 - Estado del agua
# Determina el estado fisico del agua segun su temperatura en grados Celsius.

temperatura = float(input("Ingresa la temperatura del agua en grados Celsius: "))

if temperatura <= 0:
    print("El agua esta en estado SOLIDO (hielo).")
elif temperatura < 100:
    print("El agua esta en estado LIQUIDO.")
else:
    print("El agua esta en estado GASEOSO (vapor).")
