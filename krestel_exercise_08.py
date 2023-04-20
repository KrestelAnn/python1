print("Convert a number to Roman numerals")

# Define the Roman numeral symbols and their corresponding values
roman_numerals = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

# Get input from user
num = int(input("Enter an integer between 1 and 3999: "))

# Initialize the Roman numeral string
roman_numeral = ""

# Convert the number to Roman numerals
for value, symbol in roman_numerals.items():
    while num >= value:
        roman_numeral += symbol
        num -= value

# Print the Roman numeral equivalent
print(f"The Roman numeral equivalent is: {roman_numeral}")
