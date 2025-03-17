for i in range(11):
  pass

# when we run the program you can see that it does absolutely nothing.
# loop syntax requires at least one instruction inside the loops body.
# You may be in the middle of writing your code and you don't know yet what to put inside your loops body.
# So you may start off with a pass instruction so that your code doesn't throw errors.
# By the way, the same applies to if statements all of your if Elif and else blocks must contain at least a single instruction

# nested loops 
# Take a look at this example where we show a simple multiplication table from 1 to 5.

for a in range(1, 6):
  for b in  range(1, 6):
    print(a, 'x', b, '=', a * b)

# first a starts from 1 and second loop also starts form 1 = a=1 and b=1
# b continues to loop until 6 (6 is not included) so a is 1 until b reaches to 5.
# after b finishes the first loop a=2 then it goes to b again until a finishes the Loop


# Loops with else statements.
i = 5
while i < 5:
  print(i)
  i += 1
else:
  print('else', i)
# the output: else 5
# Here the loops condition is never satisfied from the start, so we only print the else instruction.

i = 2
while i < 5:
  print(i)
  i += 1
else:
  print('else', i)
# the output
# 2
# 3
# 4
# else 5

# variable i equals to the loops condition is satisfied.
# So we enter the loop print too and increase it to three.
# We do that until I equals five and then we enter the else branch.
# else branch is always executed exactly once, no matter how many times Python enters the loops body
# The only time the else branch is not executed is when a break statement is executed inside the loops
# Break exits the loop immediately so it also skips the else branch.