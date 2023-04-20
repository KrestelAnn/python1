print("Grade Average Calculator")

# Get input from user
grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))
grade4 = float(input("Enter the fourth grade: "))

# Calculate average
average = (grade1 + grade2 + grade3 + grade4) / 4

# Print the result
print(f"The average grade is {average:.2f}")
