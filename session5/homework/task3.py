# Task 3
# Take an input of list of numbers, find and print the unique numbers.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: 1, 3, 5

numbers = input("Please enter your numbers: ").split() # take the input convert it to a list
print(numbers)
new_list = [] # create an empty list to store unique numbers
for i in numbers: # iterate through each number in the input list(numbers)
    count = 0 # county how many times the current number (i) appears in the list
    for i2 in numbers: # the inner loop iterates through the numbers list again to compare the current number(i) with every number (i2) in the list
        if i == i2: # if i matches i2 
            count +=1 # the counter(count) incremented
    if count == 1: # if the counter(count) is equal to 1, it means the current number(i) appears only once in the list.
       new_list.append(i) # in that case the number is added to the new_list
print(", ".join(new_list)) # The join() method is used to convert the new_list (which contains unique numbers) into a single string, with each number separated by a comma.


# second way with .count
numbers = input("Please enter your numbers: ").split()  # take the input convert it to a list
print(numbers)
new_list = []# create an empty list to store unique numbers
for i in numbers: # iterate through each number in the input list(numbers)
    if numbers.count(i) == 1: # The count() method is used to count how many times the current number (i) appears in the numbers list.
       new_list.append(i) # if the current number(i)s count is equal to 1 add it to the new_lis
print(", ".join(new_list)) # The join() method is used to convert the new_list (which contains unique numbers) into a single string, with each number separated by a comma.