"""POO, mensaje de clases e interacciones"""

class Animal:

    #Constructor
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo


    #Método que me permite imprimir los atributos de mi objeto
    def presentar(self):
        #print(f'Mi animal se llama {self, nombre} y su edad es {self,edad}')
        return f'Mi {self.tipo} se llama {self.nombre} y su edad es {self.edad}'
        
#Crear hogar de animales que se permite recibir animal
class HogarAnimales:

#Constructor
    def __init__(self, direccion):
        self.direccion = direccion

        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def listar_animales(self):
        for animal in self.animales:
            print(animal.presentar())
        
perro_1 = Animal('Maximus', 1, 'perro')
#print(perro_1.presentar())
gato_1 = Animal('Pelanas', 2, 'gato') 

hogar_1 = HogarAnimales('Cl 63 # 16')
    
hogar_1.agregar_animal(perro_1)
hogar_1.agregar_animal(gato_1)
hogar_1.listar_animales()
