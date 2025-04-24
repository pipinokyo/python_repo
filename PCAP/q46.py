# What is the expected behavior of the following program?

try:
    print(5/0)
    break
except:
    print("Sorry, something went wrong...")
except (ValueError, ZeroDivisionError):
    print("Too bad...")