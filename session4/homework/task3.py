# Task 3: Find the Longest Word in a List
# Ask the user to enter a list of words. Find and print the longest word from the list.
# Example:
# Enter words: Python Java JavaScript C  
# Longest word: JavaScript  

# for loop
list = input('Enter words seperated by spaces: ').split() # .split() splits the input into as list based on spaces
print("original list: ", list)
longest = '' # This variable will store the longest word found in the list.
# also if we are going to use for loop we need to compare if the length is longer than something
for i in list: # Iterates over each element (i) in the list (list).
    if len(i) > len(longest): # Compares the length of the current word (i) with the length of the current longest word
        longest = i # If the current word is longer, it updates the longest variable to store the current word.
print(longest)



# Using max() with key=len
list = input('Enter words seperated by spaces: ').split() # .split() splits the input into as list based on spaces
print("original list: ", list)
longest = max(list, key=len) # The max() function is used to find the maximum value in an iterable
# The key parameter specifies a function that is applied to each element before comparison. 
print(longest)



# Using sorted() and Indexing
list = input('Enter words seperated by spaces: ').split() # .split() splits the input into as list based on spaces
print("original list: ", list)
longest = sorted(list, key=len)[-1]# The sorted() function sorts the elements of an iterable in ascending order by default.
# [-1] refers to the last element of the list.
print(longest)