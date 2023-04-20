print("Variable Swapper (using 2 variables)")

# Get input from user
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

# Print the original values
print(f"The original values are: x = {x}, y = {y}")

# Swap the values using 2 variable declarations
x = x + y
y = x - y
x = x - y

# Print the new values
print(f"The new values are: x = {x}, y = {y}")
