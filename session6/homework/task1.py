# Task 1: Filter and Count Students by Attendance
# Write a function that takes a dictionary of students and a minimum attendance percentage.
# The function should return a dictionary containing only the students who meet or exceed the attendance requirement.

# Example:
# students_data = {
#     "101": {"name": "Alice", "attendance": 95},
#     "102": {"name": "Bob", "attendance": 88},
#     "103": {"name": "Charlie", "attendance": 92},
#     "104": {"name": "Diana", "attendance": 80},
#     "105": {"name": "Ethan", "attendance": 90},
# }

# print(filter_students_by_attendance(students_data, 90))

# Output:
# {
#     "101": {"name": "Alice", "attendance": 95},
#     "103": {"name": "Charlie", "attendance": 92},
#     "105": {"name": "Ethan", "attendance": 90}
# }
from pprint import pprint # new code to print prettier chech jason.dumps too 

students_data = {
    "101": {"name": "Alice", "attendance": 95},
    "102": {"name": "Bob", "attendance": 88},
    "103": {"name": "Charlie", "attendance": 92},
    "104": {"name": "Diana", "attendance": 80},
    "105": {"name": "Ethan", "attendance": 90},
}
def filtered_students(students_data, attendance): # we define a func named filtered_students takes two arguments
    # students_data dictionary contains all students data.
    # attendance the mininum attendance percentage threshold
    # why we used parameter instead of just a number . this way the function is reusable
    result = {} # we create an empty dictionary called result to store the filtered students 
    for i, score in students_data.items(): # we use for loop to iterate tfrough the student_date dicitonary
        # i is the key here.when you want to go through all the items in the dictionary use to variable like in this example.
        # score is the value here. score is the dictionary containing the students details
        # example i = "101" and the score = {"name": "Alice", "attendance": 95}
        if score["attendance"] > attendance: # for each student we check if their attendance (score["attendance"]) id greater than 90
            # if you wanted to check the name instead of attendance you should have put (score["name"]) 
            result[i] = score # if the student's attendance is greater than 90, we add them to the result dictionary
            # the key is the student id(i) in the first loop is 101 and the key value is score. in the first loop is {"name": "Alice", "attendance": 95}
    return result # after the loop finishes we return the result dictionary containing only the filtered students
        
attendance_thresshold = int(input('Enter the attendance threshold it is going to give you greater or equal results: '))
# we ask the user to put input for attendance 
pprint(filtered_students(students_data, attendance_thresshold))
# we use pprint here same thing with print but prettier

