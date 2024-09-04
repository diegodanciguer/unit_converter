def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def meters_to_kilometers(meters):
    return meters / 1000

def meters_to_miles(meters):
    return meters / 1609.34

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def menu():
    print("Escolha o tipo de conversão:")
    print("1. Temperatura")
    print("2. Distância")
    choice = input("Digite sua escolha (1 ou 2): ")

    if choice == "1":
        print("\nEscolha a conversão de temperatura:")
        print("1. Celsius para Fahrenheit")
        print("2. Celsius para Kelvin")
        print("3. Fahrenheit para Celsius")
        print("4. Fahrenheit para Kelvin")
        print("5. Kelvin para Celsius")
        print("6. Kelvin para Fahrenheit")
        temp_choice = input("Digite sua escolha (1-6): ")
        value = float(input("Digite o valor para converter: "))

        if temp_choice == "1":
            print(f"{value}°C = {celsius_to_fahrenheit(value)}°F")
        elif temp_choice == "2":
            print(f"{value}°C = {celsius_to_kelvin(value)}K")
        elif temp_choice == "3":
            print(f"{value}°F = {fahrenheit_to_celsius(value)}°C")
        elif temp_choice == "4":
            print(f"{value}°F = {fahrenheit_to_kelvin(value)}K")
        elif temp_choice == "5":
            print(f"{value}K = {kelvin_to_celsius(value)}°C")
        elif temp_choice == "6":
            print(f"{value}K = {kelvin_to_fahrenheit(value)}°F")
        else:
            print("Escolha inválida.")
    
    elif choice == "2":
        print("\nEscolha a conversão de distância:")
        print("1. Metros para Quilômetros")
        print("2. Metros para Milhas")
        print("3. Quilômetros para Metros")
        print("4. Quilômetros para Milhas")
        dist_choice = input("Digite sua escolha (1-4): ")
        value = float(input("Digite o valor para converter: "))

        if dist_choice == "1":
            print(f"{value} metros = {meters_to_kilometers(value)} quilômetros")
        elif dist_choice == "2":
            print(f"{value} metros = {meters_to_miles(value)} milhas")
        elif dist_choice == "3":
            print(f"{value} quilômetros = {kilometers_to_meters(value)} metros")
        elif dist_choice == "4":
            print(f"{value} quilômetros = {kilometers_to_miles(value)} milhas")
        else:
            print("Escolha inválida.")
    
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    menu()
