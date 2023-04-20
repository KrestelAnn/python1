print("Date Converter.")

# Get input from user
date = input("Enter a date in the format DD/MM/YYYY: ")

# Split the date into day, month and year
day, month, year = date.split("/")

# Convert the day and month to integers
day = int(day)
month = int(month)

# Define a list of month names
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

# Print the complete form of the date
print(f"{day} {months[month-1]} {year}")
