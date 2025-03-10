# Task 2: Reverse a Word using for loop (please don’t reverse a string using word[::-1])
# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP








# 1. take an input 
word = input('Provide a word please: ')

# 2. initialize an empty string to store the reversed word
reversed_word =''

# 3. use a for loop to iterate through each character of the word
# range(len(word) - 1, -1, -1):
# Starts at the last index (len(word) - 1). 
# Ends at -1 (but doesn’t include -1).
# Moves backward with a step of -1.
for i in range(len(word) -1, -1, -1): #because this is string we have to use len function

# word[i] gives the character at index i.
# += appends the character to reversed_word.
    reversed_word += word[i]

# and print the reversed_word
print(reversed_word)

# it was complicated check !!!this out later