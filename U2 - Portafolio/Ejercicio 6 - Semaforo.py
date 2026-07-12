# Ejercicio 6 - Semaforo
# Indica la accion a realizar segun el color del semaforo.

color = input("Ingresa el color del semaforo (rojo, amarillo o verde): ").lower()

if color == "rojo":
    print("ALTO. Debes detenerte.")
elif color == "amarillo":
    print("PRECAUCION. Disminuye la velocidad.")
elif color == "verde":
    print("SIGUE. Puedes avanzar.")
else:
    print("Color invalido. Ingresa rojo, amarillo o verde.")
