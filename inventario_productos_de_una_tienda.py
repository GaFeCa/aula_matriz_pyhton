inventario = {}


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible del producto: "))
    inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
    print("Producto agregado correctamente.")


def actualizar_cantidad():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre in inventario:
        nueva_cantidad = int(input("Ingrese la nueva cantidad disponible: "))
        inventario[nombre]['cantidad'] = nueva_cantidad
        print("Cantidad actualizada correctamente.")
    else:
        print("Producto no encontrado en el inventario.")


def mostrar_inventario():
    print("Inventario:")
    for nombre, info in inventario.items():
        precio = info['precio']
        cantidad = info['cantidad']
        print(f"Nombre: {nombre} | Precio: {precio} | Cantidad disponible: {cantidad}")


while True:
    print("\nMenú:")
    print("1. Agregar un producto")
    print("2. Actualizar cantidad de un producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    opcion = input("Ingrese la opción deseada: ")

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        actualizar_cantidad()
    elif opcion == '3':
        mostrar_inventario()
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")