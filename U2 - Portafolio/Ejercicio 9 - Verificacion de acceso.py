# Ejercicio 9 - Verificacion de acceso
# Verifica si una persona puede acceder segun su edad (mayor de edad).

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad invalida.")
elif edad >= 18:
    print("Acceso PERMITIDO. Eres mayor de edad.")
else:
    print("Acceso DENEGADO. Eres menor de edad.")
