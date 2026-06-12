# Ejercicio 1
# Crear un subproceso llamado SaludarUsuario que reciba como
# parámetro el nombre de una persona y muestre en pantalla un
# mensaje de bienvenida personalizado.

def SaludarUsuario(nombre: str) -> None:
    print(f"Bienvenido, {nombre}!")

if __name__ == "__main__":
    input_nombre = input("Ingrese su nombre: ")
    SaludarUsuario(input_nombre)