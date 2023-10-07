import os
import matplotlib.pyplot as plt
import pandas as pd

class Archivo:
    def __init__(self, nombre, tamaño, permisos):
        self.nombre = nombre
        self.tamaño = tamaño
        self.permisos = permisos

    def renombrar(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_permisos(self, nuevos_permisos):
        self.permisos = nuevos_permisos

    def eliminar(self):
        try:
            os.remove(self.nombre)
            print(f"El archivo {self.nombre} ha sido eliminado.")
        except FileNotFoundError:
            print(f"El archivo {self.nombre} no existe.")

    def __str__(self):
        return f"Archivo: {self.nombre}, Tamaño: {self.tamaño} bytes, Permisos: {self.permisos}"

class Directorio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = []

    def listar_archivos(self):
        if not self.contenido:
            return "El directorio está vacío."
        lista_archivos = "\n".join([elemento.nombre for elemento in self.contenido])
        return f"Contenido de {self.nombre}:\n{lista_archivos}"

    def crear_directorio(self, nombre):
        nuevo_directorio = Directorio(nombre)
        self.contenido.append(nuevo_directorio)
        return nuevo_directorio

    def buscar_archivos(self, nombre):
        resultados = []
        for elemento in self.contenido:
            if isinstance(elemento, Directorio):
                resultados.extend(elemento.buscar_archivos(nombre))
            elif isinstance(elemento, Archivo) and nombre in elemento.nombre:
                resultados.append(elemento)
        return resultados

    def mover_archivo(self, archivo, nuevo_directorio):
        if archivo in self.contenido:
            self.contenido.remove(archivo)
            nuevo_directorio.contenido.append(archivo)

    def __str__(self):
        return f"Directorio: {self.nombre}"

# Funciones relacionadas con archivos y directorios
def listar_archivos_en_directorio(directorio):
    return directorio.listar_archivos()

def crear_archivo(nombre, tamaño, permisos):
    return Archivo(nombre, tamaño, permisos)

def crear_directorio(nombre):
    return Directorio(nombre)

def renombrar_elemento(elemento, nuevo_nombre):
    elemento.renombrar(nuevo_nombre)

def eliminar_elemento(elemento):
    elemento.eliminar()

def buscar_archivos_en_directorio(directorio, nombre):
    resultados = directorio.buscar_archivos(nombre)
    return resultados

def mover_elemento_a_directorio(elemento, nuevo_directorio):
    nuevo_directorio.contenido.append(elemento)
    return nuevo_directorio

def cambiar_permisos_archivo(archivo, nuevos_permisos):
    archivo.cambiar_permisos(nuevos_permisos)

# Funciones relacionadas con la generación de gráficos desde un archivo CSV
def generar_grafica_desde_csv(nombre_archivo_csv, entidad_a_graficar):
    try:
        data = pd.read_csv(nombre_archivo_csv)
        entidad_data = data[data['NIT_DE_LA_ENTIDAD'] == entidad_a_graficar]

        if not entidad_data.empty:
            entidad_data.plot(kind='bar', x='AÑO', y='VALOR_TOTAL_CONTRATO')
            plt.xlabel('Año')
            plt.ylabel('Valor Total del Contrato')
            plt.title(f'Histórico de Contratación para la Entidad con NIT: {entidad_a_graficar}')
            plt.show()
            plt.savefig(f'grafica_{entidad_a_graficar}.png')
            print(f'Gráfica generada y guardada como grafica_{entidad_a_graficar}.png')
        else:
            print(f'No se encontraron datos para la entidad con NIT {entidad_a_graficar}.')
    except FileNotFoundError:
        print(f'El archivo CSV {nombre_archivo_csv} no existe.')

# Ejemplo de uso de las funciones
if __name__ == "__main__":
    # Crear archivos y directorios
    archivo1 = crear_archivo("documento.txt", 1024, "755")
    archivo2 = crear_archivo("imagen.jpg", 2048, "644")
    directorio = crear_directorio("MiDirectorio")
    directorio.contenido.append(archivo1)
    directorio.contenido.append(archivo2)

    # Listar archivos en el directorio
    print(listar_archivos_en_directorio(directorio))

    # Renombrar un archivo
    renombrar_elemento(archivo1, "nuevo_documento.txt")

    # Cambiar permisos de un archivo
    cambiar_permisos_archivo(archivo1, "777")

    # Eliminar un archivo
    eliminar_elemento(archivo2)

    # Crear un nuevo directorio
    subdirectorio = crear_directorio("SubDirectorio")

    # Mover un archivo a otro directorio
    subdirectorio = mover_elemento_a_directorio(archivo1, subdirectorio)
    print(listar_archivos_en_directorio(subdirectorio))

    # Buscar archivos por nombre
    resultados_busqueda = buscar_archivos_en_directorio(directorio, "nuevo")
    for elemento in resultados_busqueda:
        print(elemento)

    # Generar gráfica desde un archivo CSV
    generar_grafica_desde_csv("data_processed.csv", "NIT_DE_LA_ENTIDAD")