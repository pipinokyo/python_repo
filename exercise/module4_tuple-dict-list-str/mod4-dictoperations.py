# First of all, since dictionaries are mutable, we can start with an empty dictionary and then add new elements to it.
grades = {}

# adding a new element can be done with square brackets in a very simple way.
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)
# The output of the above code will be:
# {'John': 'A-', 'Anne': 'B'}

# you can update dictionary entries using the very same syntax.
grades['Anne'] = 'A'
print(grades)
# The output of the above code will be:
# {'John': 'A-', 'Anne': 'A'}

# Another option is to use the update method.
grades.update({'John': 'B'})
print(grades)
# The output of the above code will be:
# {'John': 'B', 'Anne': 'A'}

# you can use the Len function here.
print(len(grades))
# The output of the above code will be:
# 2

# To check if a given key is present in a dictionary, you can use the good old in operator.
if 'John' in grades:
    print('John got:', grades['John'])
else:
    print('John not found')
# The output of the above code will be:
# John got: B

# you can use the del operator.
del grades['John']
print(grades)
# The output of the above code will be:
# {'Anne': 'A'}

# you must know that prior to Python, 3.6 dictionaries were not ordered.
# This means that you could add key value pairs to a dictionary a certain way,
#  but Python could then store them internally in other way.
# This changed in Python 3.6 and dictionaries have now become ordered collections by default.


grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
for el in grades:
    print(el)
# The output of the above code will be:
# John
# Anne

for el in grades.keys():
  print(el)
# The output of the above code will be:
# John
# Anne

for el in grades.values():
  print(el)
# The output of the above code will be:
# A-
# B

for person, grade in grades.items():
  print(person, 'got', grade)
# The output of the above code will be:
# John got A-
# Anne got B