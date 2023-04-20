print("Yearly Depreciation Calculator")

# Get input from user
P = float(input("Enter the purchase price of the item: "))
Y = float(input("Enter the expected number of years of service: "))
S = float(input("Enter the expected salvage value: "))

# Calculate the yearly depreciation
D = (P - S) / Y

# Print the result
print(f"The yearly depreciation for the item is: {D:.2f}")
