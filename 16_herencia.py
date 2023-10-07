"""Herencia en programación orientada a objetos"""

class Animal:
    #Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Método que me permite imprimir los atributos de mi objeto

    def presentar(self):
        #print(f'Mi {self.tipo} se llama {self.nombre} y su edad es {self.edad}')
        return f'Mi animal'