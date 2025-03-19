top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
for city in top_cities:
  print('Current city:', city)
# let's analieze the code
# 1. We have a list called top_cities which contains the names of five cities.
# 2. We use a for loop to iterate over each element in the list.
# 3. The loop assigns each element to the variable city in turn.
# 4. Inside the loop, we print the current city using the print function.
# 5. The loop continues until all elements in the list have been processed.
# 6. The output will show the name of each city in the list one by one.
# The output of the code will be:
# Current city: New York
# Current city: Los Angeles
# Current city: Chicago
# Current city: Houston
# Current city: Phoenix


# There's also another way to iterate over a list in such a way that you can access both the element and its index.
top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
for city_index in range(len(top_cities)):
  print('Current index:', city_index, '| Current city:', top_cities[city_index],)

# let's analieze the code
# 1. We have a list called top_cities which contains the names of five cities.
# 2. We use the range function to create a sequence of indices from 0 to the length of the list minus one.
# 3. The loop iterates over each index in the sequence.
# 4. Inside the loop, we print the current index and the corresponding city using the print function.
# 5. The output will show the index and name of each city in the list one by one.
# The output of the code will be:
# Current index: 0 | Current city: New York
# Current index: 1 | Current city: Los Angeles
# Current index: 2 | Current city: Chicago
# Current index: 3 | Current city: Houston
# Current index: 4 | Current city: Phoenix
# 6. The loop continues until all indices in the range have been processe

# example
spendings = [32.45, 12.20, 25.45, 11.45, 21.45]
total_spendings = 0.0
for spending in spendings:
  total_spendings += spending
print('Total spendings:', total_spendings)

#  the output of the code will be:
# Total spendings: 103.00000000000001