import os

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

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear archivos y directorios
    archivo1 = Archivo("documento.txt", 1024, "755")
    archivo2 = Archivo("imagen.jpg", 2048, "644")
    directorio = Directorio("MiDirectorio")
    directorio.contenido.append(archivo1)
    directorio.contenido.append(archivo2)

    # Listar archivos en el directorio
    print(directorio.listar_archivos())

    # Renombrar un archivo
    archivo1.renombrar("nuevo_documento.txt")

    # Cambiar permisos de un archivo
    archivo1.cambiar_permisos("777")

    # Eliminar un archivo
    archivo2.eliminar()

    # Crear un nuevo directorio
    subdirectorio = directorio.crear_directorio("SubDirectorio")

    # Mover un archivo a otro directorio
    directorio.mover_archivo(archivo1, subdirectorio)

    # Buscar archivos por nombre
    resultados_busqueda = directorio.buscar_archivos("nuevo")
    for elemento in resultados_busqueda:
        print(elemento)