first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
age = input("Enter your age:")

# CConcatenate your first name and last name
full_name = first_name + " " + last_name

#Slice the full name to extract the first three characters of the first name
sliced_name = first_name[:4]

#create a greeting message that includes the sliced first name
greeting = f"Hello, {sliced_name}! Welcome. You are {age} years old."

#print the result
print("\nFull Name:", full_name)
print("Sliced Name:", sliced_name)
print("Greeting:", greeting)

