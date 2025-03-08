# Task 2: Character Type Identifier
# Ask the user to input a single character. Determine and print:
# "It's a digit" if the character is a number (0-9).
# "It's a letter" if the character is a letter (a-z, A-Z).
# "It's a special character" otherwise.


# 1. set a value with users input
# 2. check if the input is singe character if not print the input is not a single char
# 3. check if the input is a character or letter or special character
# 4. and print the result
# 5. i can use boolean and contiditions

char = input('please provide a character: ')

if len(char) != 1:
    print("please provide a single valid charachter")
elif char.isdigit():
    print("It's a digit")
elif char.isalpha():
    print("It's a letter")
else:
    print("It's a special character")

   