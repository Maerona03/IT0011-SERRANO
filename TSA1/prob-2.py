#Problem: A program that will count the sum of the digits from a given input string digits. 

def sum_digits(input_string):
    sum = 0 #initialize sum to 0
    
    #loop through the input string
    for char in input_string:
        if char.isdigit(): #check if the character is a digit
            sum += int(char) #add the digit to the sum
    print("Sum of digits: ", sum)

# User input and function call
user_input = input("Enter a string: ")
sum_digits(user_input)