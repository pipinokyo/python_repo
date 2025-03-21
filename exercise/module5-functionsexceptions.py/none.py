print('hello')

length = len('hello')
print(length)

number = input('What is the number?')  
print(number)
# # the input will be a string
# # we can convert it to an integer using the int() function

print_return = print('hello, world')
print(print_return)
# # the output will be 'hello, world'
# # and the return value will be None
# # because the print() function does not return any value


x = None

if x:
  print('none is True')
elif x is False:
  print('none is False')
else:
  print('none is not True or False')
# # the output will be 'none is not True or False'
# # because None is a special value that represents the absence of a value
# # it is not equal to False or True
# # it is a separate type of object in Python


x = None
if x is None:
  print('x is None')
if x == None:
  print('x == None')
# # the output will be:
# # x is None
# # x == None

def greet():
  print('hello')

x = greet()
print(x)
# # the output will be:
# # hello
# # None
# # because the greet() function does not return any value
# # it returns None by default