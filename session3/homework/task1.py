# # Task 1: Count Down from input number to 1

# 1. set a variable for the users input
# convert the data type to int
# 2. use a for loop with the range function:


# this function prompts the user to enter a value and convert it to an int
num = int(input('give me a number please to count down: '))

# this loop iterates over each number in this sequence.
# range(start, end, step) generates a sequence of number starting from users input
# and counting down to 1
# the -1 specifies the step size, 
for i in range(num ,0, -1): # 
# and we print until the range is over
    print(i)




# there is another way bu using while loop 

# again we take the input, set a variable and convert it to an int
num = int(input('give me a number please to count down: '))

#the while loop repeatedy executes the code inside the loop until the condition is true
while num > 0:
# we print the current value of the variable
    print(num)
# This statement decreases the value of num by 1 after each iteration of the loop.
    num -= 1 # The shorthand num -= 1 is equivalent to num = num - 1
# basically it continues as long as the contiditon is true num > 0