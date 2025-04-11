# What is the expected output of the following code?
def func(text, num):
    while num > 0:
        print(text)
    num = num - 1
        
# func('Hello', 3)

# Why It's an Infinite Loop
# Indentation Error: The num = num - 1 line is not indented properly, so it's outside the while loop

# Loop Condition Never Changes: Since we never decrement num inside the loop, num remains 3 forever

# Result: The loop keeps printing 'Hello' endlessly because num > 0 is always true

# Visualization of Execution

# Initial state:
# num = 3

# First iteration:
# num > 0 → True
# Prints "Hello"
# num remains 3 (decrement line not reached)

# Second iteration:
# num > 0 → True 
# Prints "Hello"
# num remains 3

# ... repeats forever ...