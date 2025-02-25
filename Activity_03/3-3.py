# Accept input for the last name, first name, age, contact number, and course
last_name = input("Enter Last name: ")
first_name = input("Enter First name: ")
age = input("Enter Age: ")
contact_number = input("Enter Contact number: ")
course = input("Enter Course: ")

# Create a string containing the collected information in a formatted way
student_info = f"\nLast Name: {last_name}\nFirst Name: {first_name}\nAge: {age}\nContact Number: {contact_number}\nCourse: {course}\n"

# Open a file named students.txt in append mode and write the formatted info to the file
with open("students.txt", "a") as file:
    file.write(student_info)

# Display a confirmation message indicating that the information has been saved
print("\nStudent information has been saved to 'students.txt'.")
