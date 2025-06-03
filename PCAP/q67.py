# What is the correct command to shuffle the following list?


import random
people = ['Joe', 'Bob', 'Sue', 'Sally']

# A. shuffle(people)
# B. people.shuffle( )
# C. random.shuffle(people)
# D. random.shuffleList(people)


# Analyzing the Options:

# A. shuffle(people) ❌
# Incorrect because shuffle() is not a standalone function—it must be called from the random module.
# This would raise a NameError unless shuffle was imported separately (e.g., from random import shuffle).

# B. people.shuffle() ❌
# Incorrect because Python lists do not have a built-in .shuffle() method.
# This would raise an AttributeError.

# C. random.shuffle(people) ✅
# Correct because:
# It uses the random module.
# Calls shuffle() with the correct syntax.
# Shuffles the list in-place.

# D. random.shuffleList(people) ❌
# Incorrect because there is no such function as shuffleList() in the random module.
# This would raise an AttributeError.