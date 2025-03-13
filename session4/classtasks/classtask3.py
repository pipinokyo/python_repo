lst = ["banana", True, False, "apple", 10, "pineapple", "cherry", "apple", 1, 10.3, True]
filtered_list = []
for i in lst:
    if type(i) == str: # if isinstance(i, str):
        filtered_list.append(i)
print(filtered_list)    

