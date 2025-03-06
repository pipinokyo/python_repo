# Task 4: Reverse a String
# Ask the user to enter a word and print it in reverse. (Hint: Use slicing)
# first think came to mind was to use for loop
# get the input from the user and save it to the variable word.
# create another variable and initialize an empty string to save the result of the loop
# loop every single character in word variable
# save it to the second variable in revers order by adding each character to the beginning of the new string
# and print the reversed variable

word = input("Enter a word: ")
reversed_word = ""
for character in word:
    reversed_word = character + reversed_word
print("reversed word:", reversed_word)

# and then i googled it to find a simplier way 

# word = input("enter a word: ")
# reversed_word = word[::-1]
# print("reversed word:", reversed_word)