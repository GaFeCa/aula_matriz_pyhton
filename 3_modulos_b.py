"""Crear mi propio modulo.
Servirá para hacer un cálculo aproximado de mi edad"""

def calcular_edad(anio_nacimiento,anio_actual):
    edad_aprox = anio_actual - anio_nacimiento
    print(edad_aprox)
    return edad_aprox

edad_saliente = calcular_edad(1989,2023)


print("tipo de variable", type(edad_saliente))
print(edad_saliente)