what can we do with list

1. Create a List
my_list = [1, 2, 3, 4, 5]

2. Access Elements
print(my_list[0])  # Output: 1
print(my_list[-1]) # Output: 5 (last element)

3. Modify Elements
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

4. Add Elements
You can add elements to a list using methods like append(), insert(), or extend().
my_list.append(6)        # Adds 6 to the end
my_list.insert(1, 20)    # Inserts 20 at index 1
my_list.extend([7, 8])   # Adds multiple elements
print(my_list)           # Output: [10, 20, 2, 3, 4, 5, 6, 7, 8]

5. Remove Elements
You can remove elements using methods like remove(), pop(), or del.
my_list.remove(20)  # Removes the first occurrence of 20
my_list.pop(1)      # Removes and returns the element at index 1
del my_list[0]      # Deletes the element at index 0
print(my_list)      # Output: [3, 4, 5, 6, 7, 8]

6. Slice a List
sliced_list = my_list[1:4]  # Gets elements from index 1 to 3
print(sliced_list)           # Output: [4, 5, 6]

7. Check if an item exists in a list using the in keyword.
print(5 in my_list)  # Output: True

8. Iterate Over a List
for item in my_list:
    print(item)

9. List Comprehensions
squares = [x**2 for x in my_list]
print(squares)  # Output: [9, 16, 25, 36, 49, 64]

10. Sort a List
You can sort a list using the sort() method or the sorted() function.
my_list.sort()  # Sorts the list in place
print(my_list)  # Output: [3, 4, 5, 6, 7, 8]

sorted_list = sorted(my_list, reverse=True)  # Returns a new sorted list
print(sorted_list)  # Output: [8, 7, 6, 5, 4, 3]

11. Reverse a List
You can reverse a list using the reverse() method or slicing.
my_list.reverse()  # Reverses the list in place
print(my_list)     # Output: [8, 7, 6, 5, 4, 3]

reversed_list = my_list[::-1]  # Creates a reversed copy
print(reversed_list)           # Output: [3, 4, 5, 6, 7, 8]

12. Find the Length
print(len(my_list))  # Output: 6

13. Concatenate Lists
You can combine lists using the + operator.
new_list = my_list + [9, 10]
print(new_list)  # Output: [3, 4, 5, 6, 7, 8, 9, 10]

14. Copy a List
You can create a copy of a list using the copy() method or slicing.
copied_list = my_list.copy()
copied_list = my_list[:]

15. Nested Lists
Lists can contain other lists, allowing you to create multi-dimensional structures.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6

16. Filter and Map
You can use filter() and map() functions to process lists.
# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, my_list))

# Square all elements
squares = list(map(lambda x: x**2, my_list))

17. Find Index of an Element
You can find the index of an element using the index() method.

index = my_list.index(5)
print(index)  # Output: 2

18. Count Occurrences
You can count how many times an element appears in a list using the count() method.
count = my_list.count(5)
print(count)  # Output: 1

19. Clear a List
You can remove all elements from a list using the clear() method.
my_list.clear()
print(my_list)  # Output: []

20. Convert to Other Data Structures
You can convert a list to other data structures like sets, tuples, or dictionaries.
my_set = set(my_list)
my_tuple = tuple(my_list)
print(", ".join(new_list)) # it joins all the characters in the list and you can specify the seperator here is ", "
