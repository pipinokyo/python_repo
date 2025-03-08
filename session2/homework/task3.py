# Task 3: Three-Number Maximum
# Take three integer inputs and print the largest one using only if-elif-else conditions.

# 1. I need to set 3 variable with the input that user provides
# 2. convert them into int
# 3. compare them to eact other to find the max one
# 4. i can use if-elif-else and 'and,or,not'


# # my first is this but did not work
num1 = int(input('Please provide the first number: '))
num2 = int(input('Please provide the second number: '))
num3 = int(input('Please provide the third number: '))

if num1 > num2 and num3: # the issue is num3 is treated as standolena boolean expression
# any non-zero number is considered true. so anytime i tried to run this it takes the first condition as true and print.
    print(f'{num1} is the largest number')
elif num2 > num1 and num3:
    print(f'{num2} is the largers number')
else: # num3 > num1 and num2:
    print(f'{num3} is the largers number')


# # this one works
num1 = int(input('Please provide the first number: '))
num2 = int(input('Please provide the second number: '))
num3 = int(input('Please provide the third number: '))

if num1 > num2 and num1 > num3: #This checks if num1 is greater than both num2 and num3. If true, num1 is the largest number.
    print(f'{num1} is the largest number')
elif num2 > num1 and num2 > num3: #This checks if num2 is greater than both num1 and num3. If true, num2 is the largest number.
    print(f'{num2} is the largers number')
else: # num3 > num1 and num3 > num2:If neither of the above conditions is true, then num3 must be the largest number.
    print(f'{num3} is the largers number')


# there is another way to do this
# if num1 > num2 then num2 is smaller. now we can check which number is larger between num1 and num3
# if the condition num1 > num2 then num1 is smaller
# so now we can check which number is larger between num2 and num2
# for this i am going to try to use nested if statement
num1 = int(input('Please provide the first number: '))
num2 = int(input('Please provide the second number: '))
num3 = int(input('Please provide the third number: '))

if num1 > num2:
    # num1 is smaller
    if num1 > num3:
        # num3 is smaller
        large = num1
    else:
        # num1 is smaller
        large = num3
else:
    # num1 is smaller
    if num2 > num3:
        # num3 is smaller
        large = num2
    else: 
        # num2 is smaller
        large = num3
print(f'{large} is the largers number')


# the easiest way is uning max
num1 = int(input('Please provide the first number: '))
num2 = int(input('Please provide the second number: '))
num3 = int(input('Please provide the third number: '))

large = max(num1, num2, num3)
print(large)