# Simple Calculator Program

print("Welcome to the Simple Calculator!\n")

# Get numbers from user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Oops! Please enter valid numbers.")
    exit()

# Show operation choices
print("\nSelect operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# Get user choice
choice = input("Enter choice (1/2/3/4): ")

# Perform calculation
if choice == '1':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 == 0:
        print("\nError: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
else:
    print("\nInvalid operation choice. Please enter 1, 2, 3, or 4.")        
