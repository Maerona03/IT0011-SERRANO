try:
    #user input for the date
    date_input = input("Enter the date (mm/dd/yyyy): ")

    if not date_input:
        raise ValueError("Date input cannot be empty.")

    month, day, year = date_input.split('/')

    month = int(month)
    day = int(day)
    year = int(year)

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if month not in range(1, 13):
        print("Invalid month. Please enter a value between 01 and 12.")
    elif day not in range(1, 32):
        print("Invalid day. Please enter a value between 01 and 31.")
    else:
        # Convert month to its name and format the date
        month_name = months[month - 1]
        print(f"Date Output: {month_name} {day}, {year}")

except ValueError:
    print("Invalid input. Please enter the date in mm/dd/yyyy format.")
except IndexError:
    print("Error: Month value out of range.")