print("Aircraft Type Checker.")

# Get input from user
speed = float(input("Enter the observed speed of the aircraft in km/h: "))
length = float(input("Enter the estimated length of the aircraft in meters: "))

# Define the threshold values for military aircraft
military_speed_threshold = 750
military_length_threshold = 20

# Check if the aircraft is military or civilian
if speed >= military_speed_threshold and length >= military_length_threshold:
    print("The aircraft is a military aircraft.")
else:
    print("The aircraft is a civilian aircraft.")
