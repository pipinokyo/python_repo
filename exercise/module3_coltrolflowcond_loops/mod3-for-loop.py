# for loop with string
for letter in 'hello!':
  print('current letter', letter)
# the output
# current letter h
# current letter e
# current letter l
# current letter l
# current letter o
# current letter !


for loop with integers
for counter in range(1,11):
  print(counter)
print('finished')

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# finished
# Note that the start value is inclusive in the sequence, but the stop value is exclusive.


for counter in range(11):
  print(counter)
print('finished')

# If you just provide a single number, this number will be treated as the stop value.
# The default start value of zero will be used and each generated value will be increased by one


for counter in range(2, 11, 2):
  print(counter)
print('finished')

# the output
# 2
# 4
# 6
# 8
# 10
# finished
# You can also provide three numbers, in which case the last argument will be the increase amount.