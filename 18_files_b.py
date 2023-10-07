"""Manejador de contexto para archivos

with --> Cerrar el archivo así a nosotros se nos olvide cuando termine de usarlo"""

with open('para_manejo_file.txt', mode='r+') as file:
    for line in file:
        print(line, end='')

    #Escribir el nombre de nuestro compañero fañtante 
    file.write('Leandro')


