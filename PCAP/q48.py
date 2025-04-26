# What is the expected output of the following code?

file = open('data.txt', 'w+')
print('Name of the file: ', file.name)

s = 'Peter Wellert\nHello everybody'
file.write(s)
file.seek(0)
for line in file:
    print(line)

file.close()