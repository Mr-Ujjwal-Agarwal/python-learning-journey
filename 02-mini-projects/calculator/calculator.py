# ==========================================
# Simple Calculator Using Python
# Developed by Ujjwal Agarwal
# Concepts Used:
# - while loop
# - if-elif-else
# - operators
# - user input
# - type conversion
# ==========================================

print("=" * 50)
print("        Welcome to My Calculator")
print("=" * 50)


while True:
    print("\nPlease select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

   
    choice = input("\nEnter your choice (1-5): ")

    
    if choice == "5":
        print("\nThank you for using My Calculator!")
        print("Goodbye! 👋")
        break

    
    if choice == "1" or choice == "2" or choice == "3" or choice == "4":

       
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

       
        if choice == "1":
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")

        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("\nError: Division by zero is not allowed.")

    else:
        print("\nInvalid choice! Please select a number between 1 and 5.")
