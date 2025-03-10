# Task 3: Factorial of a Number (use for loop)
# Input:
# Enter a number: 5

# Output:
# Factorial of 5 is 120


# we take the input and convert it to an integer and save it as a variable
fac = int(input('give me a number please: '))
if fac >= 0:  # if stat checks if the value of fac is greater or equal to 0
    # if so then it goes to next step
    if fac == 0: # nested if checks if the value is equal to zero
        result = 1 # if so the result is 1 becuse 0!=1 and prints the result
    else: # if it is not equal to 0 then 
        result = 1 # i made a mistake here did not put another variable so
        # we need to set a variable to intitilaize to 1 so it can add on to it and multiply
        # in this for loop we go through all the number normaly it would print all the number in order.
        # but we multiply each number with the result which is one and save the result in result variable
        for i in range(1, fac + 1 ):
            result = result * i # result *= i this is the same but shorter version
    print(f"the factorial of {fac} is {result}")
else: 
    print('The input must be  number greater or equal to 0')