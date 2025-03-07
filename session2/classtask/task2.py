# write a program that will do the following
# 1. takes integer input
# 2. checks if integer is positive 
# if the number is negative print ('hey give me positive number') 
# 3. checks if the integer is even or odd 
# prints the following :'number is even or odd'




# num1 = int(input('provide a number please: '))
# remain = num1 % 2
# if num1 >= 0 and remain == 0:
#     print('the number is even')
# elif num1 >= 0 and remain == 1:
#     print('the number is odd')
# else:
#     print('hey give me a positive number') 



num1 = int(input('provide a number please: '))
if num1 >= 0:
    if num1 % 2 == 0:
        print('the number is even')
    else:
        print('the number is odd')
else:
    print('hey give me a positive number') 