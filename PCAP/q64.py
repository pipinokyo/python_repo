# What is the expected output of the following code?

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(C, A))

# Inheritance Hierarchy:
# Let's visualize the inheritance relationship:

# A
# │
# └── B
#     │
#     └── C

# B is a direct subclass of A
# C is a direct subclass of B, which makes C an indirect subclass of A

# The issubclass() Function:
# The issubclass(class1, class2) function returns True if class1 is a subclass of class2 (direct, indirect, or virtual).

# Step-by-Step Evaluation:
# issubclass(C, A) checks if C is a subclass of A
# C directly inherits from B
# B directly inherits from A
# Therefore, C is an indirect subclass of A through B

# The function returns True

# Output:
# The code will print:
# True