def es_palindromo(frase):
    
    frase = frase.replace(" ", "").lower()
    if frase == frase[::-1]:
        print(f"La frase '{frase}' es un palíndromo.")
    else:
        raise ValueError("La frase no es un palíndromo")

try:
    frase = input("Introduzca una frase: ")
    es_palindromo(frase)
except ValueError as e:
    print(e)
