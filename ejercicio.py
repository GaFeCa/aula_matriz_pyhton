
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    while True:
        try:
            celsius = float(input("Ingresa la temperatura en grados Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")
            break  # Sale del ciclo si se ingresó un valor válido
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")

if __name__ == "__main__":
    main() 