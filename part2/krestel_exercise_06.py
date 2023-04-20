print("Earthquake Damage Estimator.")

# Get input from user
magnitude = float(input("Enter the magnitude of the earthquake: "))
depth = float(input("Enter the depth of the earthquake in kilometers: "))

# Define the damage levels dictionary
damage_levels = {
    (0.0, 2.0): "The earthquake was too small to cause any damage.",
    (2.0, 3.0): "The earthquake was felt, but caused no damage.",
    (3.0, 4.5): "The earthquake caused some damage to buildings and other structures.",
    (4.5, 6.0): "The earthquake caused significant damage to buildings and other structures.",
    (6.0, 7.0): "The earthquake caused widespread damage and destruction to buildings and other structures.",
    (7.0, float("inf")): "The earthquake caused catastrophic damage and destruction to buildings and other structures."
}

# Determine the extent of damage based on magnitude and depth
for key in damage_levels.keys():
    if magnitude >= key[0] and magnitude < key[1]:
        if depth < 70 and key != (2.0, 3.0):
            print(f"{damage_levels[key]}")
        else:
            print(f"{damage_levels[key]}, particularly those that are poorly constructed.")
