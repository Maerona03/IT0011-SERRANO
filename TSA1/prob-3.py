#Problem: A program that will display the following given output. 

def pattern_a():
    rows = 5
    print("Pattern A:\n")
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print increasing numbers
        for k in range(1, i + 1):
            print(k, end="")
        print()  # Newline for the next row

def pattern_b():
    row = 1
    print("Pattern B:\n")
    sequence = [1, 3, 5, 6, 7]  # The sequence of numbers for each row
    while row <= 5:
        # Get the current number from the sequence
        num = sequence[row - 1]
        
        # Print the number the appropriate number of times
        count = 0
        while count < num:
            print(num, end="")
            count += 1
        
        # Print leading spaces after the number
        spaces = 5 - row
        while spaces > 0:
            print(" ", end="")
            spaces -= 1
        
        print()  # Newline after each row
        row += 1




# Call both patterns
pattern_a()
print()  # Add a blank space between patterns
pattern_b()
