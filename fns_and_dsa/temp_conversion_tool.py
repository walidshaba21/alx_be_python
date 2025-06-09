FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def get_temperature():
    while True:
        temp_value = input("Enter the temperature to convert: ")
        
        if temp_value.isdigit():
            temp_value = int(temp_value)
            break
        else:
            print("Invalid temperature. Please enter a numeric value.")
    temp_conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    temp_conversion = temp_conversion.lower()
    if temp_conversion == "c":
        return convert_to_fahrenheit(temp_value)
    elif temp_conversion == "f":
        return convert_to_celcius(temp_value)


print(get_temperature()) 
                        
    
