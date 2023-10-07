"""Son objetos que se usan para iterar.

- No ocupa toda la memoria que ocuparía una función con return
- Su palabra clave es yield
- Solicitamos elementos con la palabra next"""

#def generar_valores_return(n):
 #   list = []
  #  for i in range(1,n):
   #     list.append(i)
    #return list


lista_salida = generar_valores_return(10)
print(lista_salida)

def generar_valores_return_b(n):
    
    for i in range(1,n):
        return i
        
print('Pirmera solicitud')
print(generar_valores_return_b(10))


print('Segunda solicitud')
print(generar_valores_return_b(10))


lista_salida = generar_valores_return_b(10)
print(lista_salida)




def give_values_yield(n):
    for i in range(1, n):
        yield i

num=give_values_yield(|10)
print(num)

print('Primera solicitud')
print(next(num))

x=4

print('Sedunda solicitud')
print(next(num))
    
