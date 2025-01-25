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

def temperature_conversion():
    print("Temperature Conversion Tool")
    print("Choose the source temperature unit (C for Celsius, F for Fahrenheit, K for Kelvin):")
    source_unit = input().strip().upper()

    print("Enter the temperature value:")
    temperature = float(input())

    print("Choose the target unit for conversion (C for Celsius, F for Fahrenheit, K for Kelvin):")
    target_unit = input().strip().upper()

    if source_unit == 'C':
        if target_unit == 'F':
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        elif target_unit == 'K':
            result = celsius_to_kelvin(temperature)
            print(f"{temperature}°C is {result}K")
        else:
            print("Invalid target unit")
    
    elif source_unit == 'F':
        if target_unit == 'C':
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        elif target_unit == 'K':
            result = fahrenheit_to_kelvin(temperature)
            print(f"{temperature}°F is {result}K")
        else:
            print("Invalid target unit")
    
    elif source_unit == 'K':
        if target_unit == 'C':
            result = kelvin_to_celsius(temperature)
            print(f"{temperature}K is {result}°C")
        elif target_unit == 'F':
            result = kelvin_to_fahrenheit(temperature)
            print(f"{temperature}K is {result}°F")
        else:
            print("Invalid target unit")
    
    else:
        print("Invalid source unit")

if __name__ == "__main__":
    temperature_conversion()
