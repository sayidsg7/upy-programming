# Ejercicio 7 - Categoria de IMC
# Calcula el Indice de Masa Corporal (IMC) y muestra su categoria.

peso = float(input("Ingresa tu peso en kilogramos: "))
estatura = float(input("Ingresa tu estatura en metros: "))

imc = peso / (estatura ** 2)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Categoria: Bajo peso")
elif imc < 25:
    print("Categoria: Peso normal")
elif imc < 30:
    print("Categoria: Sobrepeso")
else:
    print("Categoria: Obesidad")
