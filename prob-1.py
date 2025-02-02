#Problem: A program that will display the number of vowels, consonants, spaces, and other characters given an input string. 
def analyze_string(input_string):
    vowels = 0
    consonants = 0
    spaces = 0
    others = 0
    
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    
    for char in input_string:
        if char.isalpha():  # Check if the character is alphabetic
            if char.lower() in vowels_list:
                vowels += 1 #for vowels
            else:
                consonants += 1  #for consonants
        elif char.isspace():  # Check if it's a space
            spaces += 1 #counting spaces
        else:
            others += 1 
            #for other characters

    # Output the results
    print("Vowels: ", vowels)
    print("Consonants: ", consonants)
    print("Spaces: ", spaces)
    print("Others: ", others)

# User input and function call
user_input = input("Enter a string: ")
analyze_string(user_input)

