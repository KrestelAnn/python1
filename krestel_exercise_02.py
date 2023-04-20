print("Fahrenheit to Celcius.")

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
FAHRENHEIT_TO_CELSIUS_CONSTANT = 32

# Get input from user
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - FAHRENHEIT_TO_CELSIUS_CONSTANT) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Print the result
print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")