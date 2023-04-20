print("Variable Swapper (using 3 variables)")

# Get input from user
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

# Print the original values
print(f"The original values are: x = {x}, y = {y}")

# Swap the values using a temporary variable
temp = x
x = y
y = temp

# Print the new values
print(f"The new values are: x = {x}, y = {y}")
