# Task 4: Find the Second Largest Number in a List (No max() or sort())
# Ask the user to enter a list of numbers. Find and print the second largest number without using max() or sort().
# Example:
# Enter numbers: 10 45 78 23 89 56  
# Second largest number: 78


#example_list = ['10', '20', '30', '5', '15']
number = input('enter number: ').split() # take an input and split the string into a list
print(f'original list: {number}')
for i in range(0, len(number)): # outer loop iterates through each index i of the list
    # lets say in the first loop i will be 10 and it will go to second loop
    for j in range(i + 1, len(number)): # in this loop range will start i + 1 so it means its the second number which is 20
        if number[i] > number[j]: # so in the first loop number[i] = 10  and number[j] = 20 if 10 is bigger than 20
            temp = number[i] #  and if its not greater than which is the case here than we save it in a temp vaiable to compare for later
            number[i] = number[j] # if number[i] which is 10  equal to number[j] which is 20 then 
            number[j] = temp # number[j] which is 20 equal to temp 
print(f'sorted list: {number}')
print('the second largest number is: ', number[-2])


# not my code
#example_list = ['10', '20', '30', '5', '15']
inp = input('input: ') # Take input from the user
lis_of_num = inp.split() # Split the input into a list of strings

max_num = 0 # Initialize variable to store the maximum number
second_max = 0 # Initialize variable to store the second maximum number

for i in lis_of_num: # Loop through each number in the list at this point i is '10'
    i = int(i) # Convert the current element from string to integer at this point i is 10

    if i > max_num and i > second_max: # This condition checks if the current number (i) is greater than both max_num and second_max
        max_num = i # if true, it updates max_num to the current number.
    elif i > second_max and second_max < max_num: # This condition checks if the current number (i) is greater than second_max but less than max_num
        second_max =  i # If true, it updates second_max to the current number
# Logic: If i is greater than second_max but not greater than max_num, it means i is the new second maximum.
print(f'maximum number is: {max_num}')
print(f'second maximum number is: {second_max}')