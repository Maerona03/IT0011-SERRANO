# Accept input for student details
last_name = input("Enter Last name: ")
first_name = input("Enter First name: ")
age = input("Enter Age: ")
contact_number = input("Enter Contact number: ")
course = input("Enter Course: ")

# Create a formatted string with student details
student_info = f"""
Last Name: {last_name}
First Name: {first_name}
Age: {age}
Contact Number: {contact_number}
Course: {course}
"""

# Open the file in append mode and write student info
f = open("Activity_03/students.txt", "a")  # Using explicit file handling
f.write(student_info)
f.close()  # Ensure the file is properly closed

# Confirmation message
print("\nStudent information has been saved to 'students.txt'.")
