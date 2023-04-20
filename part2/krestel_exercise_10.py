print("Grade Equivalent Calculator")

# Get input from user
percentile = int(input("Enter percentile grade: "))

# Define grade range and equivalent
grade_range = [(90, 100), (85, 89), (80, 84), (75, 79), (70, 74), (60, 69), (0, 59)]
grade_equivalent = ["A", "B+", "B", "C+", "C", "D", "F"]

# Find the grade equivalent
for i, (start, end) in enumerate(grade_range):
    if percentile >= start and percentile <= end:
        grade = grade_equivalent[i]
        break

# Display the result
print(f"Percentile grade: {percentile}")
print(f"Grade equivalent: {grade}")
