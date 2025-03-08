# input function always returns a string even if you ask the user to provide a number.
heigth_cm = input('Height converter:enter your height in cm: ')
print('Your height in feet is:', height_cm / 30.48)# On line two, we try to show the height converted into feet
# this code will throw an error!!you can't divide a string by a float.

# this is one way to convert
heigth_cm = input('Height converter:enter your height in cm: ')
float_heigth_cm = float(heigth_cm)
print('Your height in feet is:', float_heigth_cm / 30.48)
# if you run the program will work

# this is the second option
heigth_cm = float(input('Height converter:enter your height in cm: '))
print('Your height in feet is:', height_cm / 30.48)

#you can apply the same method with in
year_born =int(input('What year were you boen?'))
print('in 2100, you will be', 2100 - year_born, 'years old,')


# if you want to conver to string simply add str instead of float or int
temp_c = input('Enter the temperature today in Celcius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celcius equals ' + str(temp_f) + 'degrees Fahrenheit'
print(temp_statement)

# Note two things In the world of computer programming type conversion,
# which means changing from strings o floats or from integers to strings is often called typecasting.
# if the users provides a name and tries to cast it to a str it will fail