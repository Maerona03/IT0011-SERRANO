def is_palindrome(number):
    return str(number) == str(number)[::-1]

def check_palindrome_sums(filename):
    
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    
    for i, line in enumerate(lines, start=1):
        numbers = [int(num) for num in line.strip().split(',') if num.strip()]
        total = sum(numbers)
        result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
        print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")

# Usage: Ensure the correct file path and filename
check_palindrome_sums(r"C:\Users\ronam\OneDrive\MIDTERM\prob-one\numbers.txt")
