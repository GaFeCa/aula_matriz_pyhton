def calcular_promedio_y_validar_primo():
    input_str = input("Ingrese una lista de valores separados por comas: ")
    valores = input_str.split(',')
    valores = [int(valor) for valor in valores if valor.strip().isdigit()]
    if not valores:
        print("La lista está vacía. No se puede calcular el promedio.")
        return
    suma = sum(valores)
    promedio = suma / len(valores)
    print(f'El valor promedio es {promedio:.1f}')
    validar_primo(int(promedio))

def validar_primo(numero):
    if numero <= 1:
        print(f'{numero} no es un número primo')
    else:
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print(f'{numero} es un número primo')
        else:
            print(f'{numero} no es un número primo')
calcular_promedio_y_validar_primo()