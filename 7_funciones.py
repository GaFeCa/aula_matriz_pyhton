"""Funciones:
Cómo declararlas y ver funcionamiento"""

def sumar(sumando1, sumando2):
    valor_suma = sumando1 + sumando2
    return valor_suma

print(sumar(5, 10))

#Restar 3 a la suma que me arroja la función

#Opcion 1 

valor_resultante_suma = sumar(5, 10)
valor_con_resta = valor_resultante_suma - 3
print(valor_con_resta)
