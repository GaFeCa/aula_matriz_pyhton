#variable_a = 7
#variable_a /= 0

#var_b = 5
#var_b += 2
#print(var_b)

#var_b = 5 
#var_b = += 2 
#print(var_b)

# while True:

try:
    variable_a = 7 
    variable_a /=0
    string_prueba = "s"
    var_result = 7 + string_prueba 

except ZeroDivisionError:
    print("Todo mal, la embarramos, casi la embarramos totalmente")
except ValueError:
    print("Todo otra vez mal")
except Exception as e:
    print (e)


print("Hola num")
