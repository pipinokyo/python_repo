# Task 4: Password Strength Checker
# Ask the user for a password input. Check and print:
# "Strong password" if the length is at least 8 characters and contains both letters and numbers.
# "Weak password" otherwise.


# 1. we need to set a variable for the users input
# 2. we can use the len() , .isdigit(), .isalpha() functions here 
# if the return is true than we will print strong password if not weak password

# # this is my first try and it did not work

password = input('Please provide your password: ')
if len(password) >= 8:
    if password.isdigit(): # The condition if password.isdigit() checks if the password consists ONLY OF DIGITS.
        if password.isalpha(): # same problem here checks if variable contains ONLY LETTER.
            print('Strong password')
    else:
        print('Weak password')
else:
    print('Weak password')
# therefore the logic is flawed


# similar problem here
#The condition password.isdigit() and password.isalpha() requires the password to be both entirely digits and entirely letters at the same time.
password = input('Please provide your password: ')
if len(password) >= 8 and password.isdigit() and password.isalpha():
    print('Strong password')
else:
    print('Weak password')


# another way to do is to check what the variable doesn't contain
# if the variable las less than 8 character its a weak password
# if the variable has at least 8 character and only contains digit then its a weak password
# if the variable has at least 8 character and only contains alpha then its a weak password
password = input("Enter your password, please: ")

if len(password) < 8:
    print("Weak password")
elif password.isdigit() or password.isalpha():
    print("Weak password")
else:
    print("Strong password")



# the most complicated way 
# since isdigit() and isalpha() check if the variable contains only letter or numnber
# i will have to use any() and to check both number and and letters i have to use for
# first i am going to check the lenght if the lenght is 8 or more we will continue 
# if not we will print weak password
# second i will need to check if variable contains letter and store the result in a variable
# same logic with the number checking


# Ask the user for a password input
password = input('Please provide your password: ')

# Check if password is at least 8 characters long
if len(password) >= 8:
    # Check if password contains at least one letter and one digit
    letter = any(char.isalpha() for char in password)
    digit = any(char.isdigit() for char in password)

    if letter and digit:
        print('Strong password')
    else:
        print('Weak password')
else:
    print('Weak password')
# understood the logic but had to steal some codes

