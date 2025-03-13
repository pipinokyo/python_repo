# Task 5: Create a Diamond Pattern
# Ask the user for a number and print a diamond shape using *.
# Example:
# Enter a number: 5  
#     *  
#    ***  
#   *****  
#  *******  
# *********  
#  *******  
#   *****  
#    ***  
#     *  



n = int(input("Enter a number: "))
s = input('what symbol so you want to use? : ')

for i in range(n): # This loop runs from 0 to n-1 (e.g., for n = 5, i takes values 0, 1, 2, 3, 4).
# It controls the number of rows in the upper half of the diamond.
    for j in range(n - i - 1):
        print(" ", end="")
 
    for k in range(2 * i + 1):
        print(s, end="")
    
    print()


for i in range(n - 2, -1, -1):
   
    for j in range(n - i - 1):
        print(" ", end="")
   
    for k in range(2 * i + 1):
        print(s, end="")
    
    print()


