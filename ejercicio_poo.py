class Cerveza:
    def __init__(self, nombre, tipo, contenido_alcohol):
        self.nombre = nombre
        self.tipo = tipo
        self.contenido_alcohol = contenido_alcohol

    def mostrar_informacion(self):
        return f'Nombre: {self.nombre} | Tipo: {self.tipo} | Contenido de alcohol: {self.contenido_alcohol}%'

class CatalogoCervezas:
    def __init__(self):
        self.cervezas = []

    def agregar_cerveza(self, cerveza):
        self.cervezas.append(cerveza)

    def mostrar_todas_las_cervezas(self):
        for cerveza in self.cervezas:
            print(cerveza.mostrar_informacion())

    def buscar_por_contenido_alcohol(self, minimo_contenido_alcohol):
        cervezas_coincidentes = []
        for cerveza in self.cervezas:
            if float(cerveza.contenido_alcohol) >= minimo_contenido_alcohol:
                cervezas_coincidentes.append(cerveza)
        return cervezas_coincidentes

    def actualizar_cervezas(self, nuevas_cervezas):
        self.cervezas = nuevas_cervezas

    def agregar_cervezas_desde_lista(self, lista_de_cervezas):
        self.cervezas.extend(lista_de_cervezas)

class IPA(Cerveza):
    def __init__(self, nombre, contenido_alcohol):
        super().__init__(nombre, 'IPA', contenido_alcohol)

class Lager(Cerveza):
    def __init__(self, nombre, contenido_alcohol):
        super().__init__(nombre, 'Lager', contenido_alcohol)

class Producto:
    def __init__(self, nombre, costo_pesos_colombianos, precio):
        self.nombre = nombre
        self.costo_pesos_colombianos = costo_pesos_colombianos
        self.precio = precio

    def ganancia_obtenida(self):
        return self.precio - self.costo_pesos_colombianos

    def __str__(self):
        return f'Nombre: {self.nombre} | Costo en Pesos Colombianos: {self.costo_pesos_colombianos} | Precio de venta: {self.precio}'


cerveza_1 = IPA('Aguila', '5.0')
cerveza_2 = Lager('Club Colombia', '4.5')
cerveza_3 = IPA('Budweiser', '6.5')
cerveza_4 = Lager('Heineken', '5.0')


catalogo = CatalogoCervezas()


catalogo.agregar_cerveza(cerveza_1)
catalogo.agregar_cerveza(cerveza_2)
catalogo.agregar_cerveza(cerveza_3)
catalogo.agregar_cerveza(cerveza_4)


print("Catálogo completo:")
catalogo.mostrar_todas_las_cervezas()


minimo_contenido_alcohol = float(input("Ingrese el valor mínimo de contenido de alcohol: "))


cervezas_coincidentes = catalogo.buscar_por_contenido_alcohol(minimo_contenido_alcohol)


print(f"\nCervezas con contenido de alcohol igual o superior a {minimo_contenido_alcohol}%:")
for cerveza in cervezas_coincidentes:
    print(cerveza.mostrar_informacion())


cerveza_5 = IPA('Corona', '4.7')
cerveza_6 = Lager('Pilsen', '4.2')
nuevas_cervezas = [cerveza_5, cerveza_6]


catalogo.actualizar_cervezas(nuevas_cervezas)


print("\nCatálogo actualizado:")
catalogo.mostrar_todas_las_cervezas()


producto_1 = Producto('Aguila', 2500, 5000)
producto_2 = Producto('Club Colombia', 3000, 6500)


print(f"\nGanancia obtenida del producto 1: {producto_1.ganancia_obtenida()}")


print("\nLista de cervezas con precio de venta:")
for cerveza in catalogo.cervezas:
    print(cerveza.mostrar_informacion())
    for producto in [producto_1, producto_2]:
        if cerveza.nombre == producto.nombre:
            print(f"  - {str(producto)}")  