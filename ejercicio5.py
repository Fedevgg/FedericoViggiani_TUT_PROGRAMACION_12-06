# Ejercicio 5
# Crear un programa que llene un vector con 5 números enteros.
# Diseñar una Función llamada BuscarMayor que reciba ese vector
# como parámetro, lo recorra, encuentre cuál es el número más grande y
# lo devuelva para ser mostrado en el programa principal.

vector: list[int] = []
for i in range(5):
    vector.append(int(input(f"Ingrese el numero {i+1}: ")))

def BuscarMayor(vector: list[int]) -> int:
    mayor = vector[0]
    for numero in vector:
        if numero > mayor:
            mayor = numero
    return mayor

if __name__ == "__main__":
    print(f"El numero mayor es: {BuscarMayor(vector)}")
