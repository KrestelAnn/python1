print("Tuition Fee Calculator")

# Get input from user
units = int(input("Enter number of units: "))
mode = input("Enter mode of payment (full, installment): ")

# Define constants
FULL_PAYMENT_DISCOUNT = 0.1
INSTALLMENT_FEE = 0.05
TUITION_FEE_PER_UNIT = 1000

# Calculate tuition fee
tuition_fee = units * TUITION_FEE_PER_UNIT

# Apply discount for full payment
if mode == "full":
    discount = tuition_fee * FULL_PAYMENT_DISCOUNT
    tuition_fee -= discount

# Add installment fee for installment payment
elif mode == "installment":
    installment_fee = tuition_fee * INSTALLMENT_FEE
    tuition_fee += installment_fee

# Display the result
print(f"Total tuition fee: {tuition_fee:.2f}")
