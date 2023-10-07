"""Uso de diccionarios"""

import random

paises = ["col", "ecu", "bol"]
#{"col": 50, "ecu": 20, "bol": 10}

dict_poblacion_pais = {}

for pais in paises:
    dict_poblacion_pais[pais] = random.randint(9,60)

print(dict_poblacion_pais)

print(dir(dict_poblacion_pais))

print("Obtener items: ", dict_poblacion_pais.items())
print("Obtener items: ", dict_poblacion_pais.keys())
print("Obtener items: ", dict_poblacion_pais.values())
print("Obtener items: ", dict_poblacion_pais.pop("col"))
print(dict_poblacion_pais)

for key, value in dict_poblacion_pais.items():
    print(key, value)

#Sumatorio de poblaciones
