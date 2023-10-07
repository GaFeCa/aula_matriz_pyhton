"""Crear catalogo de cervezas"""


class Beer:

    def __init__(self, nombre, tipo, contenido_alcohol):
        self.nombre = nombre
        self.tipo = tipo
        self.contenido_alcohol = contenido_alcohol

    def show_beers(self):
        return f'Cerveza : {self.nombre} | tipo : {self.tipo} | contenido_alcohol : {self.contenido_alcohol}'

class Catalogue:
    
    def __init__(self, product_group):
        self.product_group = product_group
        self.beer_list = []

    def add_beer(self, beer):
        self.beer_list.append(beer)

    def catalogue_show_beers(self):
        for beer in self.beer_list:
            print(beer.show_beers())
    
    def alcohol_group_filter(self, alcohol_input):
        for beer in self.beer_list:
            if beer.contenido_alcohol > alcohol_input:
                print(beer.show_beers())

        

beer_1 = Beer('Aguila', 'comun', 3.5)
beer_2 = Beer('Club Colombia', 'rubia', 4.5)
beer_3 = Beer('Budweiser', 'roja', 6.5)
beer_4 = Beer('Heineken', 'negra', 7.5)

catalogue_1 = Catalogue('Cervezas')

catalogue_1.add_beer(beer_1)
catalogue_1.add_beer(beer_2)
catalogue_1.add_beer(beer_3)
catalogue_1.add_beer(beer_4)

catalogue_1.catalogue_show_beers()

alcohol_input = float(input('Ingrese el valor de alcohol para obtener las cervezas '+' que son mayores a ese valor en su contenido de alcohol:'))

catalogue_1.alcohol_group_filter(alcohol_input)


#Acceso a atributos de un objeto
print(beer_1.nombre)
print(beer_2.contenido_alcohol)

#Caracteristicas de un objeto
print(beer_1.__dict__)




