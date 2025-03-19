# create a simple list
# ask user for an index an return the value of the list
# students = ['Alice', 'Bob', 'Charlie']

# please enter an index: 4
# output : error: index out of range


students = ['Alice', 'Bob', 'Charlie']
inp = input("Please enter an index: ")
inp = int(inp)
try:
    print(students[inp])
except IndexError:
    print("Error: index out of range")  # output if index is out of range

