# What is the expected output of the following code?
class Economy:
    def __init__(self):
        self.econ_attr = True

class Business(Economy):
    def __init__(self):
        super().__init__()
        self.bush_attr = False

econ_a = Economy()
econ_b = Economy()
bush_a = Business()
bush_b = bush_a

print(isinstance(bush_a, Economy) 
      and isinstance(econ_a, Business), end="")
print(bush_b is bush_a or econ_a is econ_b)




# Expected Output
# The output will be: FalseTrue

# Which corresponds to option C. 1 | False True (assuming "1 |" is a typo or question numbering)

# Explanation
# Class Structure

# [ Economy Class ]
# +-------------------+
# | __init__()        |
# |   self.econ_attr = True |
# +-------------------+
#        ↑
#        | Inheritance
# [ Business Class ]
# +-------------------+
# | __init__()        |
# |   super().__init__() |
# |   self.bush_attr = False |
# +-------------------+
# Object Relationships
# Inheritance: Business inherits from Economy, so every Business instance is also an Economy instance.

# Object Creation:

# econ_a and econ_b are two separate Economy instances

# bush_a is a Business instance

# bush_b is assigned to reference the same object as bush_a

# Evaluation Breakdown
# First Print Statement:

# print(isinstance(bush_a, Economy) and isinstance(econ_a, Business), end="")
# isinstance(bush_a, Economy) → True (Business inherits from Economy)

# isinstance(econ_a, Business) → False (Economy doesn't inherit from Business)

# True and False → False

# end="" prevents newline between prints

# Second Print Statement:
# print(bush_b is bush_a or econ_a is econ_b)
# bush_b is bush_a → True (they reference the same object)

# econ_a is econ_b → False (different objects)

# True or False → True

# Visualization

# Object References:
# bush_a → [Business object]
#            ↑
# bush_b ────┘

# econ_a → [Economy object 1]
# econ_b → [Economy object 2]

# Evaluation Steps:
# 1. isinstance(bush_a, Economy) → True
# 2. isinstance(econ_a, Business) → False
#    → (True and False) → False
# 3. bush_b is bush_a → True
# 4. econ_a is econ_b → False
#    → (True or False) → True

# Final Output: "FalseTrue"