try:
    f = open("Activity_03/students.txt", "r")  # Open the file in read mode
    student_info = f.read().strip()  # Read the content and remove leading/trailing whitespace
    f.close()  # Close the file explicitly

    if not student_info:  # Check if the file is empty
        print("No student information found in 'students.txt'.")
    else:
        print("\nReading Student Information:")
        print(student_info)

except FileNotFoundError:  # Handle case when the file does not exist
    print("Error: 'students.txt' not found.")
except PermissionError:
    print("Error: You don't have permission to access 'students.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
