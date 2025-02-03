first_term = int(input("Enter the first term: "))
last_term = int(input("Enter the last term: "))

if first_term > last_term:
    first_term, last_term = last_term, first_term

total_sum = 0

for number in range(first_term, last_term + 1):
    total_sum += number

print(f"The sum of the numbers from {first_term} to {last_term} is {total_sum}")
