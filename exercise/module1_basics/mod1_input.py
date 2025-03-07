print('What is your name? ')
user_name = input()
print('Hello,', user_name)

# What is your name? 
# cuneyt
# Hello, cuneyt


# The input function always returns a string value.
# don't forget to convert it if you need to!!!
user_name = input('What is your name? ')
print('Hello,', user_name)


# Practising input()
# Ask the user to provide their login and native language. Use the following prompts:

# Enter your login: << remember to add a space at the end of this prompt!
# Enter your native language: << remember to add a space at the end of this prompt!

# Then, show the user the following message:

# Your login is {login provided} and you speak {language provided}

# For example, if the user provides the login h_potter and language British English, show:

# Your login is h_potter and you speak British English

# Watch out for typos: you must show the output in this particular format!

# Note: Use the "Run tests" button to check your solution and mark it as complete.
#  Do NOT use the "Run code" button as it will most likely show an error if you use an input() statement.


login = input('Enter your login: ')
language = input('Enter your native language: ')
 
print('Your login is', login, 'and you speak', language)