class Beer:
    def __init__(self, nombre, tipo, contenido_alcohol):
        self.nombre = nombre
        self.tipo = tipo
        self.contenido_alcohol = contenido_alcohol

    def show_beers(self):
        return f'Cerveza: {self.nombre} | Tipo: {self.tipo} | Contenido de alcohol: {self.contenido_alcohol}'

class Catalogue:
    def __init__(self, product_group):
        self.product_group = product_group
        self.beer_list = []

    def add_beer(self, beer):
        self.beer_list.append(beer)

    def catalogue_show_beers(self):
        for beer in self.beer_list:
            print(beer.show_beers())

    def search_by_alcohol_content(self, min_alcohol_content):
        matching_beers = []
        for beer in self.beer_list:
            if float(beer.contenido_alcohol[:-1]) >= min_alcohol_content:
                matching_beers.append(beer)
        return matching_beers

beer_1 = Beer('Aguila', 'común', '3.5%')
beer_2 = Beer('Club Colombia', 'rubia', '4.5%')
beer_3 = Beer('Budweiser', 'roja', '6.5%')
beer_4 = Beer('Heineken', 'negra', '7.5%')

catalogue_1 = Catalogue('Cervezas')

catalogue_1.add_beer(beer_1)
catalogue_1.add_beer(beer_2)
catalogue_1.add_beer(beer_3)
catalogue_1.add_beer(beer_4)

# Mostrar todas las cervezas en el catálogo
print("Catálogo completo:")
catalogue_1.catalogue_show_beers()

# Buscar cervezas con un contenido de alcohol igual o superior al 5.5%
min_alcohol_content = 5.5
matching_beers = catalogue_1.search_by_alcohol_content(min_alcohol_content)

# Mostrar las cervezas encontradas
print(f"\nCervezas con contenido de alcohol igual o superior al {min_alcohol_content}%:")
for beer in matching_beers:
    print(beer.show_beers())