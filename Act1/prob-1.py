num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2:
    if num1 >= num3:
        highest = num1
    else:
        highest = num3
else:
    if num2 >= num3:
        highest = num2
    else:
        highest = num3
        
        print("The highest number is", highest)