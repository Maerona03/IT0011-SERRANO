try:
    with open("students.txt", "r") as file:
      student_info = file.read().strip()
    
    if not student_info:
        print("No student information found in 'students.txt'.")
    else:
        print("\nReading student Information:")
        print(student_info)
except FileNotFoundError:
    print("No student information found in 'students.txt'.")