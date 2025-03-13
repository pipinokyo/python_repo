secret_password = 'Python123'
password = input('input: ')
while secret_password != password:
    password = input('wrong passowrd. please try again: ')
    if password == secret_password:
        print('true')