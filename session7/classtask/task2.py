# take an input of a name
# output the score of the score

# use try-except block to handle if student does not exist
# output: the studend does not exist


students_data = {"Alice": 95, "Bob": 88, "Charlie": 92, "Ethan": 90, "Diana": 80}

inp = input("Enter the name of the student: ")
try:
    print(f"{inp}'s score is {students_data[inp]}")
except KeyError:
    print(f"Student named {inp} does not exist.")

