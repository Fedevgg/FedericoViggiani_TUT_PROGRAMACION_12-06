# Ejercicio 2
# Desarrollar una función llamada CalcularDoble que reciba un número
# entero como parámetro, calcule su doble (multiplicado por 2) y
# devuelva ese resultado al programa principal para mostrarlo.

def CalcularDoble(numero: int) -> int:
    return numero * 2

if __name__ == "__main__":
    input_numero = int(input("Ingrese un numero: "))
    print(CalcularDoble(input_numero))