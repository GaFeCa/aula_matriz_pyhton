
"""Crear catalogo de cervezas"""

class Product:

    def __init__(self, name, cost, price):
        self.name = name
        self.__cost = cost
        self.price = price

    def gains(self):

        gain_per_product = self.price - self.__cost

        return f'La ganancia por venta del producto : {self.name} | es $ {gain_per_product} por unidad' 

class Beer(Product):

    def __init__(self, name, cost, price, type, alcohol_pcte):
        super().__init__(name, cost, price)
        self.type = type
        self.alcohol_pcte = alcohol_pcte

    def show_beers(self):
        return f'Cerveza : {self.name} | tipo : {self.type} | precio venta : {self.price} |contenido_alcohol : {self.alcohol_pcte} %'
    
class Ipa(Beer):

    def __init__(self, name, cost, price, alcohol_pcte, type = 'Ipa'):
        super().__init__(name, cost, price, type, alcohol_pcte)
   

class Lager(Beer):

    def __init__(self, name, cost, price, alcohol_pcte, type = 'Lager'):
        super().__init__(name, cost, price, type, alcohol_pcte)
      

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
            if beer.alcohol_pcte > alcohol_input:
                print(beer.show_beers())

    def empty_inventory(self, list_in):

        self.beer_list = list_in

## instancias --> name, cost, price, type, alcohol_pcte

beer_1 = Beer('Aguila', 2500, 4500, 'comun', 3.5)
beer_2 = Beer('Club Colombia',  3500, 5500, 'rubia', 4.5)
beer_3 = Beer('Budweiser', 4000, 6000, 'roja', 6.5)
beer_4 = Beer('Heineken',  7000, 9500, 'negra', 7.5)

# instanciando Ipa y Lager

beer_5 = Ipa('Cordillera', 3800, 6000, 2.5)
beer_6 = Ipa('Poker', 3000, 3500, 3.5)
beer_7 = Ipa('Corona', 5800, 9000, 7.5)

beer_8 = Lager('Redds', 3800, 6000, 1.5)
beer_9 = Lager('Stella Artois', 4800, 5500, 3.46)
beer_10 = Lager('Pilsen', 2000, 4200, 4.8)

catalogue_1 = Catalogue('Cervezas')


beers_to_add = [beer_1, beer_2, beer_3, beer_4, beer_5, beer_6, beer_7, beer_8, beer_9, beer_10]

for beer in beers_to_add:
    catalogue_1.add_beer(beer)

catalogue_1.catalogue_show_beers()

alcohol_input = float(input('Ingrese el valor de alcohol para filtrar las cervezas : '))

catalogue_1.alcohol_group_filter(alcohol_input)

gain_per_beer = beer_1.gains()

# entrega la ganancia para todas las cervezas del catalogo
for beer in catalogue_1.beer_list:
    print(beer.gains())
# entrega la ganancia para una cerveza en especifico
""" 
specific_beer = catalogue_1.beer_list[0]  # Cambia el índice según la cerveza que desees
gain_per_specific_beer = specific_beer.gains()
print(gain_per_specific_beer)

"""


print('Se vaciara el catalogo')

# limpiar catalogo

empty_list = []

catalogue_1.empty_inventory(empty_list)

catalogue_1.catalogue_show_beers()

print('Catalogo vacio')


# se instancia por consola

# Crear un catálogo vacío
catalogue_1 = Catalogue('Cervezas')

while True:
    # Solicitar al usuario ingresar información de la cerveza
    name = input('Ingrese el nombre de la cerveza (o "salir" para terminar): ')
    
    if name.lower() == 'salir':
        break
    
    cost = float(input('Ingrese el costo de la cerveza: '))
    price = float(input('Ingrese el precio de venta de la cerveza: '))
    type = input('Ingrese el tipo de cerveza Ipa, Lager o normal: ')
    alcohol_pcte = float(input('Ingrese el contenido de alcohol en la cerveza (%): '))
    
    # Crear una nueva instancia de Beer con la información ingresada y agregarla al catálogo
        # Verificar el tipo de cerveza y crear la instancia correspondiente
    if type.lower() == 'ipa':
        new_beer = Ipa(name, cost, price, alcohol_pcte)
    elif type.lower() == 'lager':
        new_beer = Lager(name, cost, price, alcohol_pcte)
    else:
        new_beer = Beer(name, cost, price, type, alcohol_pcte)

    catalogue_1.add_beer(new_beer)

# Mostrar todas las cervezas en el catálogo
catalogue_1.catalogue_show_beers()

# entrega la ganancia para todas las cervezas del catalogo
for beer in catalogue_1.beer_list:
    print(beer.gains())