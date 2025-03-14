# task:
# find the square numbers from 0 - 10


inp = int(input('number: '))
square = [i * i for i in range(1, inp + 1)]
# for i in range(10):
#     square.append(i * i)
print(square)


