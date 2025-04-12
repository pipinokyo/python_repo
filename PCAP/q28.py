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