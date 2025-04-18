# Which of the following lines contain valid Python code? (Select two answers.)

A. 1  |   lambda(a,b): return a if a < b else b 
B. 1  |   lambda a,b: a if a < b else b 
C. 1  |   lambda a,b = a if a < b else b 
D. 1  |   lambda a,b: True 


# Explanation of Valid Python Lambda Functions
# Let's analyze each option to determine which are valid Python lambda expressions:

# Key Characteristics of Python Lambda Functions:
# Lambda functions are anonymous functions defined with the lambda keyword

# Syntax: lambda arguments: expression

# Cannot include statements (like return) - only expressions

# Cannot have default arguments unless specified properly

# Option-by-Option Analysis:
# Option A: lambda(a,b): return a if a < b else b
# ❌ Invalid because:

# Parentheses around parameters are incorrect (should be lambda a, b:)

# Contains a return statement (lambdas can only have expressions)

# Corrected version would be: lambda a, b: a if a < b else b

# Option B: lambda a,b: a if a < b else b
# ✅ Valid because:

# Proper lambda syntax

# Uses a conditional expression (valid in lambdas)

# Equivalent to: def anonymous(a, b): return a if a < b else b

# Option C: lambda a,b = a if a < b else b
# ❌ Invalid because:

# This is trying to use a and b in the default value before they're defined

# Default arguments must be constants or defined before the lambda

# Syntax is completely wrong for a lambda function

# Option D: lambda a,b: True
# ✅ Valid because:

# Proper lambda syntax

# Simple expression that always returns True

# Equivalent to: def anonymous(a, b): return True