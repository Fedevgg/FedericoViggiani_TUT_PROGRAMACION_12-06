# Ejercicio 3
# Crear una función llamada SumarNumeros que reciba dos números
# reales, los sume y devuelva el total. El programa principal debe pedir
# los dos números, usar la función y mostrar el resultado.

def SumarNumeros(numero1: float, numero2: float) -> float:
    return numero1 + numero2

if __name__ == "__main__":
    input_numero1 = float(input("Ingrese el primer numero: "))
    input_numero2 = float(input("Ingrese el segundo numero: "))
    print(SumarNumeros(input_numero1, input_numero2))