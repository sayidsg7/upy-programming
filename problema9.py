# Problema 9: Sistema de login con usuario y contrasena

usuario = input("Ingresa el usuario: ")
contrasena = input("Ingresa la contrasena: ")

if usuario == "admin":
    if contrasena == "1234":
        print("Bienvenido")
    else:
        print("Contrasena incorrecta")
else:
    print("Usuario desconocido")
