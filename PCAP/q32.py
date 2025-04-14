# What will be the output of the following code snippet?

d = {}
d[1] = 1
d['1'] = 2
d[1] += 1

sum = 0

for k in d:
    sum += d[k]

print(sum)

# Explanation Step by Step:

# Initialize Dictionary d:

# d = {} creates an empty dictionary.

# Add Key-Value Pairs:

# d[1] = 1 assigns the value 1 to the integer key 1. Now, d = {1: 1}.

# d['1'] = 2 assigns the value 2 to the string key '1'. Now, d = {1: 1, '1': 2}.

# Note: 1 (integer) and '1' (string) are treated as distinct keys.

# Update Value for Key 1:

# d[1] += 1 increments the value of the integer key 1 by 1. Now, d = {1: 2, '1': 2}.

# Initialize sum:

# sum = 0 initializes a variable to accumulate the sum of values.

# Iterate Over Dictionary and Sum Values:

# The loop for k in d iterates over each key in d.

# For each key k, sum += d[k] adds the corresponding value to sum:

# First iteration: sum = 0 + 2 (value for key 1).

# Second iteration: sum = 2 + 2 (value for key '1').

# Print the Result:
# print(sum) outputs the total sum of the values in d, which is 4.

# Final Output:
# 4