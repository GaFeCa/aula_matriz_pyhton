"""Listas en python"""

lista_frutas = ["pera", "manzana", "durazno"]

print(dir(lista_frutas))

#Adicionar item
lista_frutas.append("banano")
print(lista_frutas)

lista_frutas.pop(2)
print(lista_frutas)

lista_nueva_frutas = sorted(lista_frutas)
print(lista_nueva_frutas)

#lista_frutas.sort()
print(lista_frutas)

lista_ascii = ["a", 5, 5.0, True]
print(lista_ascii)

for item in lista_frutas:
    print(item)
    if item == "pera":
        print("La", item, "es mi fruta favorita")
        