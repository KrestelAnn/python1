print("Temperature Checker.")

# Define the temperature threshold values
low_temp = 0
high_temp = 30

# Get the temperature from the user
temp = float(input("Enter the temperature in Celsius: "))

# Check the temperature and display a message based on its value
if temp < low_temp:
    print("It's freezing outside! Make sure to wear warm clothes.")
elif temp >= low_temp and temp <= high_temp:
    print("The temperature is just right! Enjoy your day.")
else:
    print("It's hot outside! Stay cool and hydrated.")
