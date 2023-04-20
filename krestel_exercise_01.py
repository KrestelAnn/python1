print("Feet to Centimeters.")

FEET_TO_CM = 30.48  # Conversion factor from feet to centimeters. 1feet = 30.48cm

# Get input from user
feet = float(input("Enter a length in feet: "))

# Convert feet to centimeters
centimeters = feet * FEET_TO_CM

# Print the result
print(f"{feet:.2f} feet = {centimeters:.2f} centimeters")
