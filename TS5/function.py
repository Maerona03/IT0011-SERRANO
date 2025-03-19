def divide(a, b):
    while b == 0:
        print("Error: Division by zero is not allowed.")
        b = int(input("Enter the second number: "))
    return a / b


def exponentiation(a, b):
    return a ** b


def remainder(a, b):
    while b == 0:
        print("Error: Division by zero is not allowed.")
        b = int(input("Enter the second number: "))
    return a % b


def summation(a, b):
    while a > b:
        print("Error: The second number must be greater than the first number.")
        b = int(input("Enter the second number: "))
    return sum(range(a, b + 1))


def math_program():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))
                
                if choice == 'D':
                    result = divide(a, b)
                elif choice == 'E':
                    result = exponentiation(a, b)
                elif choice == 'R':
                    result = remainder(a, b)
                elif choice == 'F':
                    result = summation(a, b)
                
                print("Result:", result)
            except ValueError:
                print("Error: Please enter valid numbers.")
        else:
            print("Error: Invalid choice. Please select a valid option.")

math_program()