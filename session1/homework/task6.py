# Task 6: Palindrome Checker
# Ask the user to enter a word and check whether it reads the same forward and backward (e.g., "madam" is a palindrome).

# The answer should return True or False


# define a variable(word) and assign it given string
# convert the string case to lowercase
# get the lenght of the string
# start looping to get each characters 
# define another variable(backword) to save to output of the loop 
# and check if word and backword are equal
# if so print True
 

# word = input("enter a word: ")
# word = word.lower()
# length = len(word)
# backword = ""
# for i in range(length - 1, -1, -1):
#     backword += word[i]
# if word == backword:
#     print(True)
# else:
#     print(False)

# ^^had to google some of it^^


# here is the shortest answer to it 
word = input("enter a word: ")
palindrome = word == word[::-1]
print(palindrome)