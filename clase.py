"""Programación orientada a objetos"""

class Animal:

    #Constructor de clase
    def __init__(self, edad, raza):
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        print(f"{self.raza} va a comer galletas")

#Intanciar clase. Declarar el objeto
perro = Animal(1, "Maximus")
print(perro.ladrar())