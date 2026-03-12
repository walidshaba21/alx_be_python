FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def get_temperature():
    while True:
        try:
            temp_value = float(input("Enter the temperature to convert: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number")

    while True:
        temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        temp_type = temp_type.lower()
        if temp_type == "c":
            result = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {result}°F")
            break
        elif temp_type == "f":
            result = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {result}°C")
            break
        else:
            print("Enter a valid temperature type")

get_temperature()