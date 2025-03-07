age = 28 
print('age')
# 28


age = 28
new_age = age + 5
print(new_age)
# 33


# The new value will be reassigned to the same variable named age and the old value will be gone.
age = 28 
age = age +7 
print(age)
# 33


# this is the short cut to set a new variable to over write
age = 28 
age += 7 
print(age)
# 33


# different ways to use it
age *= 2 # 28 * 2 = 56
age -= 5 # 28 - 5 = 23 
age /= 3 # 28 / 3 = 9.33


# string concatenation.
# The plus operator is used to join two strings together 
text = 'hokus' + 'pokus'
print(text)
# hokuspokus :!!no space! Python concatenates strings as they are without adding anything in between.


#you can also multiply a string by an integer in python.
print('hello' * 5) 
# hokushokushokushokushokus it will write it 5 time with no space

print(23 + 5) # its 28 be careful with the data type
print('23' + '5') # its 235 because these are strings