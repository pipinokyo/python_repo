# Task 2:
# Take an input and count the occurrences of each character.
# Input: programming
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}


inp = input('input: ') # we took the input

list = {} # create an empty list to can store the characters of the string

for char in inp: # we iterate through each character

    if char in list: # we check if the character exist in the list
        list[char] += 1 # increment the count if the char in the list
    else:
        list[char] = 1 # keep the same value if char is not in the list
print(list)