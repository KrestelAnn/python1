print("Vowel or Consonant Checker.")

# Get input from user
letter = input("Enter a letter: ")

# Convert letter to lowercase
letter = letter.lower()

# Check if the letter is a vowel or consonant
if letter in ['a', 'e', 'i', 'o', 'u']:
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")
