try:
    with open("students.txt", "r") as file: #Open the "students.txt" file in read mode
      student_info = file.read().strip() # Read the entire content of the file and remove leading/trailing whitespace
    
    if not student_info: # Check if the file is empty
        print("No student information found in 'students.txt'.")
    else:  # Display the student information
        print("\nReading student Information:")
        print(student_info)
except FileNotFoundError: # Handle the case where the file does not exist
    print("No student information found in 'students.txt'.")
