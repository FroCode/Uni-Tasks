def convert_temperature(value, unit):
    if unit.lower() == 'celsius':
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
    elif unit.lower() == 'fahrenheit':
        celsius = (value - 32) * 5/9
        kelvin = (value - 32) * 5/9 + 273.15
    elif unit.lower() == 'kelvin':
        celsius = value - 273.15
        fahrenheit = (value - 273.15) * 9/5 + 32
    else:
        return "Invalid unit. Please use Celsius, Fahrenheit, or Kelvin."

    return f"{value} {unit} is approximately {celsius:.2f} Celsius, {fahrenheit:.2f} Fahrenheit, and {kelvin:.2f} Kelvin."

# Example usage:
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the temperature unit (Celsius, Fahrenheit, or Kelvin): ")

result = convert_temperature(temperature, unit)
print(result)
