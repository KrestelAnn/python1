print("Ship Class Identifier.")

# Get input from user
class_id = input("Enter the class ID of the ship: ")

# Define the ship classes
ship_classes = {
    'DD': 'Destroyer',
    'CG': 'Cruiser',
    'BB': 'Battleship',
    'CV': 'Aircraft Carrier'
}

# Check the ship class and display the corresponding message
if class_id in ship_classes:
    print(f"The ship is a {ship_classes[class_id]}.")
else:
    print("The ship class is not recognized.")
