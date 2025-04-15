# What is the expected output of the following code?

class Cat:
    Species = 1
    
    def get_species(self):
        return 'kitty'

class Tiger(Cat):
    def get_species(self):
        return 'tiggy'
    
    def set_species(self):
        pass

creature = Tiger()
print(hasattr(creature, "Species"),
      hasattr(Cat, "set_species"))


# Explanation with Visualization
# 1. Class Hierarchy

# Cat (base class)
#   │
#   ├── Class variable: Species = 1
#   │
#   └── Method: get_species() → returns 'kitty'
#       ↑
# Tiger (derived class)
#   │
#   ├── Overrides get_species() → returns 'tiggy'
#   │
#   └── New method: set_species() (does nothing)
# 2. Object Creation and Attribute Checks

# creature = Tiger()  # Creates a Tiger instance
# print(hasattr(creature, "Species"),      # Checks if creature has "Species"
#       hasattr(Cat, "set_species"))       # Checks if Cat class has "set_species"
# Visualization
# Class Definitions:

# Cat:
#   - Species: 1 (class variable)
#   - get_species(): returns 'kitty'

# Tiger (inherits from Cat):
#   - get_species(): overridden to return 'tiggy'
#   - set_species(): new method
# Instance Creation:

# creature (Tiger instance):
#   - Inherits class variable Species from Cat
#   - Has overridden get_species()
#   - Has new set_species()
# Attribute Checks:

# hasattr(creature, "Species"):

# Checks creature's class hierarchy for "Species"

# Finds it in Cat class → True

# hasattr(Cat, "set_species"):

# Checks Cat class for "set_species"

# Only Tiger has it → False

# Output
# The script will output: True False