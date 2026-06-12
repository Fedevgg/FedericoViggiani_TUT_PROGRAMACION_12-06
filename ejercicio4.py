# Ejercicio 4
# Crear un subproceso llamado DibujarLinea que no reciba ningún
# parámetro. Cada vez que se lo llame, debe imprimir una línea de
# asteriscos (*******) para separar secciones en la pantalla de forma
# prolija.

def DibujarLinea() -> None:
    print("*******")

if __name__ == "__main__":
    while True:
        input_crudo = input("Presione Y para dibujar una linea, o N para salir\n")
        input_opcion = input_crudo.upper().strip()
        if input_opcion == "N":
            break
        if input_opcion == "Y":
            DibujarLinea()
        else:
            print("Opcion no valida")
