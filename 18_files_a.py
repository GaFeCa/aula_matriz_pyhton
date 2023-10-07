"""Manejo de archivos
Apertura, escritura, modificacion"""

#Apertura de archivo con signación al objeto file
file = open('para_manejo_files.txt', encoding = 'UTF8')

print(file)
#print(file.readline())
#print(file.readline())
print(file.read())
#Cierre de archivo
file.close()
