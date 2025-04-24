# What is the expected behavior of the following program?

try:
    print(5/0)
    break
except:
    print("Sorry, something went wrong...")
except (ValueError, ZeroDivisionError):
    print("Too bad...")

# Try Block:

# try:
#     print(5/0)  # Division by zero
#     break       # This line is unreachable
# 5/0 will raise a ZeroDivisionError

# The break statement is unreachable because the error occurs first

# break would be invalid here anyway (only valid in loops)

# Exception Handling:

# except:
#     print("Sorry, something went wrong...")
# except (ValueError, ZeroDivisionError):
#     print("Too bad...")
# The first except: catches ALL exceptions (including ZeroDivisionError)

# The second more specific except will never be reached because the first one catches everything

# This is poor exception handling structure (general except should come last)

# Key Problems:

# The break statement is invalid outside a loop (would cause SyntaxError if reached)

# The order of except blocks is incorrect (specific exceptions should come first)

# However, the ZeroDivisionError occurs before break is evaluated

# Expected Behavior
# The program will:

# Attempt to execute print(5/0)

# Immediately raise a ZeroDivisionError

# Be caught by the first generic except block

# Print "Sorry, something went wrong..."

# The second except block will never be reached

# The break statement is never evaluated (so no SyntaxError occurs)

# Visualization
# Start
#   │
#   ↓
# Enter try block
#   │
#   ↓
# Execute print(5/0) → Raises ZeroDivisionError
#   │
#   ↓
# (break statement never reached)
#   │
#   ↓
# Jump to first except block (generic)
#   │
#   ↓
# Print "Sorry, something went wrong..."
#   │
#   ↓
# (second except block skipped)
#   │
#   ↓
# End
# Correct Answer
# A. The program will raise an exception handled by the first except block.