import os
import shutil

class File:
    def __init__(self, path):
        self.path = path

    def list_contents(self):
        try:
            with os.scandir(self.path) as entries:
                return [entry.name for entry in entries]
        except FileNotFoundError:
            return f"Directorio '{self.path}' no encontrado."
    
    def create(self):
        try:
            with open(self.path, 'w'):
                return f"Archivo '{self.path}' creado correctamente."
        except FileExistsError:
            return f"El archivo '{self.path}' ya existe."
    
    def rename(self, new_name):
        try:
            os.rename(self.path, os.path.join(os.path.dirname(self.path), new_name))
            self.path = os.path.join(os.path.dirname(self.path), new_name)
            return f"Archivo renombrado a '{new_name}'."
        except FileNotFoundError:
            return f"Archivo '{self.path}' no encontrado."
    
    def delete(self):
        try:
            os.remove(self.path)
            return f"Archivo '{self.path}' eliminado correctamente."
        except FileNotFoundError:
            return f"Archivo '{self.path}' no encontrado."
    
    def search(self, filename):
        results = []
        for root, _, files in os.walk(self.path):
            if filename in files:
                results.append(os.path.join(root, filename))
        return results

    def move(self, destination):
        try:
            shutil.move(self.path, destination)
            self.path = destination
            return f"Archivo movido a '{destination}'."
        except FileNotFoundError:
            return f"Archivo '{self.path}' no encontrado."
    
    def change_permissions(self, permissions):
        try:
            os.chmod(self.path, int(permissions, 8))
            return f"Permisos de '{self.path}' cambiados a {permissions}."
        except FileNotFoundError:
            return f"Archivo '{self.path}' no encontrado."


class Directory:
    def __init__(self, path):
        self.path = path

    def list_contents(self):
        try:
            with os.scandir(self.path) as entries:
                return [entry.name for entry in entries]
        except FileNotFoundError:
            return f"Directorio '{self.path}' no encontrado."
    
    def create(self):
        try:
            os.makedirs(self.path)
            return f"Directorio '{self.path}' creado correctamente."
        except FileExistsError:
            return f"El directorio '{self.path}' ya existe."
    
    def rename(self, new_name):
        try:
            os.rename(self.path, os.path.join(os.path.dirname(self.path), new_name))
            self.path = os.path.join(os.path.dirname(self.path), new_name)
            return f"Directorio renombrado a '{new_name}'."
        except FileNotFoundError:
            return f"Directorio '{self.path}' no encontrado."
    
    def delete(self):
        try:
            shutil.rmtree(self.path)
            return f"Directorio '{self.path}' eliminado correctamente."
        except FileNotFoundError:
            return f"Directorio '{self.path}' no encontrado."

# Ejemplo de uso:
if __name__ == "__main__":
    file = File("example.txt")
    print(file.create())
    print(file.list_contents())
    print(file.rename("new_example.txt"))
    print(file.list_contents())
    print(file.delete())

    directory = Directory("my_directory")
    print(directory.create())
    print(directory.list_contents())
    print(directory.rename("new_directory"))
    print(directory.list_contents())
    print(directory.delete())