# task 1
# create a function that takes an integer input and prints if it's a odd or even '
# my_func(10) --> this is even number
# my_func(5) --> this is odd number

# def my_func(num):
#     if num % 2 == 0:
#         print("this is even number")
#     else:
#         print("this is odd number")

# my_func(10)
# my_func(9)   

# what is the difference between print() and return
# print() --> to output the values
# return --> only used in functions | the purpose is return outputs data type back


# task 2
# create a function that takes list of integers
# return the list of even number

# def even(num):
#     even_list = []
#     for i in num:
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst2 = [46, 12, 97, 56,43, 1, 37]
# lst3 = [311, 81, 93, 100, 56]

# print(even(lst))
# print(even(lst2))
# print(even(lst3))



# take an input of word and character and return an index of this character
# if no character is available return "No such character"

# input: my_func('akumosolutions', 'l')
# output: 7

# input: my_func('akumosolutions', 'z')
# output: "No such character"


def characterChecker(word, character):
    if character in word:
        return word.index(character)
    else:
        return "No such character"

print(characterChecker("akumosolutions", "o"))
print(characterChecker("akumosolutions", "z"))