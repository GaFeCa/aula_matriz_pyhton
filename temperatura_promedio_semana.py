
temperaturas_semana = {}


dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
for dia in dias_semana:
    temperatura = float(input(f"Ingrese la temperatura para el día {dia}: "))
    temperaturas_semana[dia] = temperatura


if "miércoles" in temperaturas_semana:
    print(f"La temperatura del miércoles fue: {temperaturas_semana['miércoles']} grados Celsius")
else:
    print("No se registró temperatura para el miércoles")

temperaturas_semana["lunes"] = 18

temperaturas = list(temperaturas_semana.values())
promedio = sum(temperaturas) / len(temperaturas)
print(f"El promedio de las temperaturas de la semana fue: {promedio:.2f} grados Celsius")


dias_calurosos = [dia for dia, temperatura in temperaturas_semana.items() if temperatura > 16]
print("Días en los que la temperatura máxima superó los 16 grados Celsius:")
print(dias_calurosos)
