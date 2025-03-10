# Task 5: Print a Word in a Pyramid Shape
# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

# # take the input from the user
# word = input('Provide a word please: ')
# # set and empty variable so we can build add the loop results in to this
# pyramid = ""
# # with the for loop we go through each character 
# for i in word:
#     # here we add each character to each other and change the pyramid in every loop
#     pyramid += i
#     # we can print i to we can see how loop works
#     print(pyramid)



# this is not my code but putting it here to understand
# Step 1: Take input from the user
word = input("Enter a word: ")

for i in range(1, len(word) + 1):
    print(word[:i])