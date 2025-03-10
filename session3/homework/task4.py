# # secret password = Python123
# # Input:

# # Enter the password: hello
# # Wrong password. Try again.

# # Enter the password: python
# # Wrong password. Try again.

# # Enter the password: Python123
# # Access Granted!

# first thing came to my mind was while loop but first i am going to try for loop



# the first try 
secret_password = ('Python123')
password = input('please provide your password: ')

if password != secret_password:
    print('Wrong password. Try again.')
    for i in range(3):
        (input('please provide your password: '))
else:
    print('Access Granted!')
# it gives 4 attemts with the first input and it does not break the loop so this does not work


# # second try it works but i think i can improve this
# to many conditions
secret_password = ('Python123')
password = input('please provide your password: ')

if password != secret_password:
    print('Wrong password. Try again.')
    for i in range(2):
        (input('please provide your password: '))
        if password == secret_password:
            print('Access Granted!')
            break
else:
    print('Access Granted!')

# 3rd try improved version
# the correct password stored in variable so we can compare with the input
# secret_password = ('Python123')
# we set for loop and set the range from 3 to 0(0 not inclued) and goes back by 1(-1)
# it loops max three times from 3 to 0
for i in range(3, 0, -1):
    # in every loop its ask the user to input their password
    # and we save the password in a variable so we can compare
    password = input(f'you have {i} attemps please provide your password: ')
    # we need to check if the input equal to secret password
    if password == secret_password:
         # if so it prints access granted and breaks the loop
         print('Access Granted!')
         break
   # here we are checking we the loop is if it is the last try we print this
    elif i == 1:
        print('sorry you are out of attemps')
        break
    else:
        # here we check if the user providing the right answer
        print(f'Wrong password.Try again. ')


# while loop answer
# while loop basically loop until the condition is true
# with while loop it will give attemps until the attemps is 0 and until password is true

# define the secret password
secret_password = ('Python123')
# set the number of attemps
attemps = 3
# while loop runs as long as attemp is greater than 0
while attemps > 0:
    # asking the user provide their passwors
    password = input(f'you have {attemps} attemps please provide your password: ')
    # if the password is equal the secret password we break the loop
    if password == secret_password:
       print("Access Granted!")
       break
    else:
        # if not we decrement the attemps counter by 1
        attemps -= 1 #  this is shorter versinon of attemps = attemps - 1
        # we check if the attemps counter is greater than 0 if so we contiue
        if attemps > 0:
            print('Wrong password. Try again.')
            # if not we finish the loop and print the following
        else:
            print("Access denied. No more attempts left.")
