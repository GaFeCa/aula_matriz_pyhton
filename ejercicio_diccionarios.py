entrada = input("Ingrese una lista de números separados por comas: ")
valores = [int(valor.strip()) for valor in entrada.split(',')]
frecuencia = {}
for valor in valores:
    if valor in frecuencia:
        frecuencia[valor] += 1
    else:
        frecuencia[valor] = 1
items_mayor_a_3 = [(clave, valor) for clave, valor in frecuencia.items() if valor > 3]
print("Diccionario de frecuencia:")
print(frecuencia)
print("Items con frecuencia mayor a 3:")
print(items_mayor_a_3)