def get_day(user_info):
    day = int(input('What is the day of your bday? '))
    user_info.append(day)

def get_month(user_info):
    month = int(input('What is the month (1-12) of your bday? '))
    user_info.append(month)

def get_year(user_info):
    year = int(input('What is the year of your bday? '))
    user_info.append(year)

def get_birthday(user_info):
    try:
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
    except ValueError:
         print('Please enter a valid number for your birthday.')

print('I will colloct your birthday information.')
user_info = []
get_birthday(user_info)

# the output will be:
# I will colloct your birthday information.
# What is the day of your bday? 15
# What is the month (1-12) of your bday? 8
# What is the year of your bday? 1990
# the user input is stored in the user_info list
# user_info = [15, 8, 1990]

# if the user enters an invalid number, the program will print an error message
# and ask the user to enter a valid number
# for example, if the user enters 'hello' for the day, the program will print:
# Please enter a valid number for your birthday.


# But how is it possible that a single try except statement here get_birthday function handles all the exceptions
# The rule is that exceptions are propagated through functions in python.