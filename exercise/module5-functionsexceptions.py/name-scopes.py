def show_truth():
  mysterious_var = 'New Surprise!'
  print(mysterious_var)

mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)

# # the output will be:
# # Surprise!
# # New Surprise!
# # Surprise!
# # the variable mysterious_var inside the function is a local variable
# # and it only exists within the scope of the function.

def show_truth():
  global mysterious_var
  mysterious_var = 'New Surprise!'
  print(mysterious_var)

mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)  
# # the output will be:
# # Surprise!
# # New Surprise!
# # New Surprise!
# # the variable mysterious_var inside the function is a global variable
# # and it can be accessed from outside the function.

def show_truth():
  mysterious_var.append('New Surprise!')
  print(mysterious_var)

mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)
# # the output will be:
# # ['Surprise!']
# # ['Surprise!', 'New Surprise!']
# # ['Surprise!', 'New Surprise!']
# # the variable mysterious_var inside the function is a mutable object