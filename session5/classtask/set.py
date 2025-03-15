what can we do with set 

In Python, a set is an unordered collection of unique elements.
Sets are highly efficient for membership tests, removing duplicates,
and performing mathematical set operations like union, intersection,
and difference. Here are some common operations and things you can do with sets:

1. Create a Set
You can create a set by enclosing elements in curly braces {} or using the set() constructor.
my_set = {1, 2, 3, 4, 5}
empty_set = set()  # Use this for an empty set ({} creates an empty dictionary)

2. Add Elements
You can add elements to a set using the add() method.
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

To add multiple elements, use the update() method.
my_set.update([7, 8, 9])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

3. Remove Elements
You can remove elements using remove(), discard(), or pop().
remove() raises an error if the element doesn't exist.
discard() does not raise an error if the element doesn't exist.
pop() removes and returns an arbitrary element.

my_set.remove(5)  # Removes 5
my_set.discard(10)  # No error even though 10 doesn't exist
popped_element = my_set.pop()  # Removes and returns an arbitrary element

4. Check for Membership
You can check if an element exists in a set using the in keyword.
print(3 in my_set)  # Output: True

5. Iterate Over a Set
You can loop through a set using a for loop.
for item in my_set:
    print(item)

6. Find the Length
You can find the number of elements in a set using the len() function.
print(len(my_set))  # Output: 8

7. Remove All Elements
You can clear a set using the clear() method.
my_set.clear()
print(my_set)  # Output: set()

8. Copy a Set
You can create a shallow copy of a set using the copy() method.
copied_set = my_set.copy()

9. Set Operations
Sets support mathematical set operations like union, intersection, difference, and symmetric difference.

Union (| or union())
Combines elements from two sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

Intersection (& or intersection())
Finds common elements between two sets.
intersection_set = set1 & set2  # or set1.intersection(set2)
print(intersection_set)  # Output: {3}

Difference (- or difference())
Finds elements in the first set that are not in the second set.
difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)  # Output: {1, 2}

Symmetric Difference (^ or symmetric_difference())
Finds elements that are in exactly one of the sets.
symmetric_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(symmetric_diff_set)  # Output: {1, 2, 4, 5}

10. Subset and Superset
You can check if one set is a subset or superset of another.
set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))  # Output: True
print(set2.issuperset(set1))  # Output: True

11. Remove Duplicates from a List
Sets are often used to remove duplicates from a list.
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)
print(unique_elements)  # Output: {1, 2, 3, 4, 5}

12. Frozen Sets
A frozenset is an immutable version of a set. It can be used as a key in a dictionary or as an element in another set.
frozen = frozenset([1, 2, 3])
print(frozen)  # Output: frozenset({1, 2, 3})

13. Set Comprehensions
You can create sets concisely using set comprehensions.
squares = {x**2 for x in range(5)}
print(squares)  # Output: {0, 1, 4, 9, 16}

14. Check Disjoint Sets
You can check if two sets have no common elements using the isdisjoint() method.
set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # Output: True

15. Convert to Other Data Structures
You can convert a set to a list, tuple, or other data structures.
my_list = list(my_set)
my_tuple = tuple(my_set)

16. Mathematical Operations
Sets are ideal for performing mathematical operations like union, intersection, and difference, as shown earlier.
    
17. Efficient Membership Testing
Sets are optimized for checking whether an element is present, making them faster than lists for this purpose.
if 3 in my_set:
    print("3 is in the set")

18. Remove Common Elements
You can remove elements from one set that are also present in another set using the difference_update() method.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}

19. Update with Intersection
You can update a set to keep only elements found in both sets using the intersection_update() method.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)  # Output: {3}

20. Symmetric Difference Update
You can update a set to keep only elements that are in exactly one of the sets using the symmetric_difference_update() method.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 4, 5}