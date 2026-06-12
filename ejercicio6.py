# Ejercicio 6
# Crear una matriz de 2x3 cargada con números automáticos y diseñar
# un Subproceso llamado ImprimirMatriz que reciba la matriz por
# parámetro y se encargue de dibujarla ordenadamente.
import random

def generarMatriz() -> list[list[int]]:
    return [[random.randint(1, 100) for _ in range(3)] for _ in range(2)]

def ImprimirMatriz(matriz: list[list[int]]) -> None:
    for fila in matriz:
        for numero in fila:
            print(numero, end=" ")
        print()

if __name__ == "__main__":
    matriz = generarMatriz()
    print("Matriz generada: \n")
    ImprimirMatriz(matriz)