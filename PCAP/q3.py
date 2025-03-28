# What is the value type returned after executing the following snippet?
x = 0
y = 2
z = len(“Python”)
x = y > z
print(x)


'''
Initial Assignments:
x = 0 → x is an integer (int) with value 0.
y = 2 → y is an integer (int) with value 2.

Calculate z:
z = len("Python") → The string "Python" has 6 characters, so z = 6 (type int).

Comparison y > z:
y > z → 2 > 6 → This evaluates to False (a boolean value, bool).

Assign Result to x:
x = y > z → x = False → x is now a boolean (bool).

Print x:
print(x) → Outputs False (which is of type bool).
'''