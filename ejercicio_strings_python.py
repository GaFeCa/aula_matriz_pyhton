import random
import string

def generar_contraseña():
    # Definir las categorías de caracteres
    caracteres_mayusculas = string.ascii_uppercase
    caracteres_minusculas = string.ascii_lowercase
    digitos = string.digits
    caracteres_especiales = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Elegir al menos un carácter de cada categoría
    contraseña = random.choice(caracteres_mayusculas)
    contraseña += random.choice(caracteres_minusculas)
    contraseña += random.choice(digitos)
    contraseña += random.choice(caracteres_especiales)

    # Generar el resto de la contraseña aleatoriamente
    longitud_restante = 8 - len(contraseña)
    todos_los_caracteres = caracteres_mayusculas + caracteres_minusculas + digitos + caracteres_especiales
    contraseña += ''.join(random.choice(todos_los_caracteres) for _ in range(longitud_restante))

    # Mezclar la contraseña para mayor aleatoriedad
    contraseña_lista = list(contraseña)
    random.shuffle(contraseña_lista)
    contraseña = ''.join(contraseña_lista)

    return contraseña

# Generar y mostrar la contraseña
contraseña_generada = generar_contraseña()
print("La contraseña generada es:", contraseña_generada)
