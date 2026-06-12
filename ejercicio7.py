# Ejercicio 7
# Desarrollar una Función llamada ValidarClave que no recibe
# parámetros pero le pide al usuario que ingrese una contraseña. Si la
# contraseña es "UTN2026", la función devuelve Verdadero. Si se
# equivoca, tiene hasta 3 intentos en total. Si se agotan los intentos y no
# acertó, devuelve Falso. El programa principal debe usar esta función
# para permitir o denegar el acceso.

def ValidarClave() -> bool:
    for i in range(3):
        input_clave = input("Ingrese la contraseña: ")
        if input_clave == "UTN2026":
            return True
        else:
            print("Contraseña incorrecta")
            print(f"Intento {i+1} de 3")
    return False

if __name__ == "__main__":
    if ValidarClave():
        print("Acceso permitido")
    else:
        print("Acceso denegado")