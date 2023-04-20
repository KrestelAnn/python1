print("Basic Arithmetic Calculator")

# Get input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate sum, difference, product, and quotient
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

# Print the results
print(f"The sum of {num1} and {num2} is {sum:.2f}")
print(f"The difference of {num1} and {num2} is {difference:.2f}")
print(f"The product of {num1} and {num2} is {product:.2f}")
print(f"The quotient of {num1} and {num2} is {quotient:.2f}")
