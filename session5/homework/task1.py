# Task 1:
# Given a dictionary of students and their scores, print only the students who scored more than 50.
# Dictionary: students = {"Alice": 45, "Bob": 78, "Charlie": 52, "David": 33}
# Output: Bob : 78, Charlie : 52

students = {"Alice": 45, "Bob": 78, "Charlie": 52, "David": 33}
for key, value in students.items(): # if we want to check both key and values we put .item as well
    if value > 50:
        print(key,':', value)