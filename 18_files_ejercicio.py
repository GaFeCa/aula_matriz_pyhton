"""Se requiere crear un rpograma para llevar el registro de los premios entregados a los 2 primeros lugares de la liga BetPlay. Cada premio se registra con el nombre del equipo, el valor del premio, la posición ocapada y el año y semestre en que fue entregado, por tanto, se debe:

1. Crear un archivo de texto llamado 'premiacion.txt
2. Generar bloques especializados de código (funciones) pára las actividades mencionadas:

- Registrar premios. Cada premio ingresado debe ser escrito en una nueva.
- Consultar: Mostrar en pantalla todas las premiaciones y el detalle
- Calcular el valor total de las premioaciones:Retoma el valor total.
- Por favor, para que sea intuitivo para el usuario , generar un menú con opciones:

Beienvenido al reporteadorm de pemios liga BetPlay. Escoja la opcion:

1. Registrar premio 
2. Consultar premio
3. Calcular total de premios
4. Salir"""



def registrar_premio():
    equipo = input("Nombre del equipo: ")
    valor = float(input("Valor del premio: "))
    posicion = int(input("Posición: "))
    anio_semestre = (input("Año: "))


    with open("premiacion.txt", "a") as archivo:
        archivo.write(f"{equipo}, {valor}, {posicion}, {anio_semestre}\n")


def consultar_premios():
    try:
        with open("premiacion.txt", "r") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay premios registrados.")
            else:
                for linea in lineas:

                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        print(f"Equipo: {datos[0]}, Valor: {datos[1]}, Posición: {datos[2]}, Periodo: {datos[3]}")
                    else:
                        print(f"Formato incorrecto en la línea: {linea}")
    except FileNotFoundError:
        print("No se encontró el archivo de premiación.")


def calcular_total_premios():
    try:
        with open("premiacion.txt", "r") as archivo:
            lineas = archivo.readlines()
            total = 0.0  

            for linea in lineas:
                datos = linea.strip().split(", ")
                if len(datos) >= 2:
                    
                    if datos[1].replace(",", "", 1).replace(".", "", 1).isdigit():
                        total += float(datos[1].replace(",", "").replace(".", "").replace(" ", ""))

            print(f"El valor total de los premios es: {total}")
    except FileNotFoundError:
        print("No se encontró el archivo de premiación.")


def main():
    while True:
        print("Bienvenido al reporteador de premios Liga BetPlay. Escoja la opción:")
        print("1. Registrar premio")
        print("2. Consultar premios")
        print("3. Calcular total de premios")
        print("4. Salir")
        
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            registrar_premio()
        elif opcion == "2":
            consultar_premios()
        elif opcion == "3":
            calcular_total_premios()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()