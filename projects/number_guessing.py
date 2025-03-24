# to generate a random number. import this module. this is default.
import random

top_of_range = input("Type a number: ")
# this is to check if the input is digit
if top_of_range.isdigit():
    # if so we convert it to an int
    top_of_range = int(top_of_range)
# here we check if the user input is less than zero
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        # quit is finishing the program
        quit()
else:
    print('Please type a number next time.')
    quit()
print(f'The number will be between 1 and {top_of_range}')
# randon.randit is to generate a random  number
# (0, top_of_range) 0 is the start point top_of_range is finish
# it will generate a number between 0 and top_of_range
random_number = random.randint(0, top_of_range)
# this guesses tracks how many guesses you used
guesses = 0

# 
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        # continue to keep running the program
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")