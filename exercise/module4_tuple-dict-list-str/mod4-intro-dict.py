# Dictionaries are collections used to store key value pairs.
# dictionaries are created with curly brackets
# inside you provide key value pairs separated by a colon
# and each key value pair is separated by a comma.
# You can't provide a value to find its key.

emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter Small': 'psmall@gmail.com',
    'John Doe': 'jdoe@gmail.com'
}
print(emails['Anne Stahl'])
# The output of the above code will be:
# astahl@gmail.com

spanish_animals = {
    'dog': 'perro',
    'cat': 'gato',
    'bird': 'pájaro',
    'fish': 'pez'
}
print(spanish_animals['dog'])
# The output of the above code will be:
# perro

print(spanish_animals['perro'])  # This will raise a KeyError because 'perro' is not a key in the dictionary.

# In both of our examples, the keys were strings, but the keys can also be of any other immutable data
#  You could have, for instance, integers, floats or even tuples as keys, but not lists.
#  So this is possible.
tennis_ranking = {
    1: 'Roger Federer',
    2: 'Rafael Nadal',
    3: 'Novak Djokovic',
    4: 'Andy Murray'
}
print(tennis_ranking)
# The output of the above code will be:
# {1: 'Roger Federer', 2: 'Rafael Nadal', 3: 'Novak Djokovic', 4: 'Andy Murray'}

#  But this is not possible.
# tennis_ranking = {
#     [1]: 'Roger Federer',
#     [2]: 'Rafael Nadal',
#     [3]: 'Novak Djokovic',
#     [4]: 'Andy Murray'
# }
# This will raise a TypeError because lists are mutable and cannot be used as dictionary keys.
#  Dictionaries are mutable, so you can add or remove key value pairs.
#  You can also change the value of an existing key.
#  Let's say we want to add a new animal to our Spanish dictionary.
spanish_animals['horse'] = 'caballo'
print(spanish_animals)
# The output of the above code will be:
# {'dog': 'perro', 'cat': 'gato', 'bird': 'pájaro', 'fish': 'pez', 'horse': 'caballo'}
#  Now let's say we want to change the value of the key 'cat'.
spanish_animals['cat'] = 'felino'
print(spanish_animals)
# The output of the above code will be:
# {'dog': 'perro', 'cat': 'felino', 'bird': 'pájaro', 'fish': 'pez', 'horse': 'caballo'}
#  And finally, let's say we want to remove the key 'fish'.
del spanish_animals['fish']
print(spanish_animals)
# The output of the above code will be:
# {'dog': 'perro', 'cat': 'felino', 'bird': 'pájaro', '
# 'horse': 'caballo'}
#  You can also use the pop method to remove a key value pair and return its value.
removed_value = spanish_animals.pop('bird')
print(removed_value)
# The output of the above code will be:
# pájaro
print(spanish_animals)
# The output of the above code will be:
# {'dog': 'perro', 'cat': 'felino', 'horse': 'caballo'}