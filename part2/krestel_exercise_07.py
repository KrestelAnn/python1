print("Number to Word Converter.")

# Define lists for the number words
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# Get input from user
num = int(input("Enter a number between 0 and 999: "))

# Define a function to convert the number to its word form
def number_to_word(num):
    if num == 0:
        return "zero"
    if num < 0 or num > 999:
        return "invalid number"

    words = ""

    # Define dictionary for switch-case
    switcher = {
        1: "one", 2: "two", 3: "three",
        4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine",
    }

    # Handle hundreds place
    if num >= 100:
        words += switcher.get(num // 100, "") + " hundred "
        num %= 100

    # Define dictionary for switch-case
    switcher = {
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 
        19: "nineteen",
    }

    # Handle tens place
    if num >= 10 and num < 20:
        words += switcher.get(num, "") + " "
        num = 0
    elif num >= 20:
        words += tens[num // 10] + " "
        num %= 10

    # Define dictionary for switch-case
    switcher = {
        1: "one", 2: "two", 3: "three",
        4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine",
    }

    # Handle ones place
    if num > 0:
        words += switcher.get(num, "")

    return words.strip()

# Convert the number to its word form and print the result
result = number_to_word(num)
print(f"The word form of {num} is {result}.")
