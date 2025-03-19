# we have the following list with integers.
book_rating = [7, 9, 5, 6, 8]
# #  let's say we want to add a new rating to the list.
# #  we can use the append method to add a new element to the end of the list.
book_rating.append(10) # this will add the rating 10 to the end of the list
# # Now we can print the list again to see if the new rating has been added
print(book_rating) # this will return [7, 9, 5, 6, 8, 10]

# There's also another method which can be used to add an element in other places in the list.
# #  the insert method allows you to add an element at a specific index in the list.
book_rating.insert(2, 4) # this will add the rating 4 at index 2
# # Now we can print the list again to see if the new rating has been added
print(book_rating) # this will return [7, 9, 4, 5, 6, 8, 10]
# #  you can also use the insert method to add an element at the beginning of the list.
book_rating.insert(0, 3) # this will add the rating 3 at index 0
# # Now we can print the list again to see if the new rating has been added
print(book_rating) # this will return [3, 7, 9, 4, 5, 6, 8, 10]