# Ejercicio 5 - Descuentos de taquilla
# Calcula el precio de un boleto de cine aplicando descuentos segun la edad.
# Ninos (menores de 12): 50% de descuento
# Adultos mayores (60 o mas): 30% de descuento
# Resto: precio completo

PRECIO_BASE = 100.0

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad invalida.")
elif edad < 12:
    precio = PRECIO_BASE * 0.50
    print(f"Descuento del 50% (nino). Precio a pagar: ${precio:.2f}")
elif edad >= 60:
    precio = PRECIO_BASE * 0.70
    print(f"Descuento del 30% (adulto mayor). Precio a pagar: ${precio:.2f}")
else:
    precio = PRECIO_BASE
    print(f"Sin descuento. Precio a pagar: ${precio:.2f}")
