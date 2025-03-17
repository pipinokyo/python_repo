# When Python encounters a break instruction, it immediately exits the loop and moves on to the next instruction outside the loop.

while True:
  name = input('Enter your name or exit to close the program: ')
  if (name == 'exit'):
    break
  print('Hello ', name)

# Instead of exiting the whole loop, continue is used to escape the current iteration and move on to the next one.
# Continue is also typically used with if statements when we sometimes want to skip a certain iteration.

# we want to show all numbers from 1 to 20 except for those that can be divided by five.
for i in range(1, 21):
  if i % 5 == 0:
    continue
  print(i)

# it will skip the number 5 and multiples of 5