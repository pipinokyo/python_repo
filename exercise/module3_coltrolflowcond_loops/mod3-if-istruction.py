user_age = int(input("what is your age? "))
if user_age > 30:
    print('you are over 30 years old')
    print('sorry, you do not qualify')
# If you forget about indentation on the last line, Python will not treat the second print invocation If you forget about indentation on the last line, Python will not treat the second print invocation


user_age = int(input("what is your age? "))
if user_age > 30:
    print('you are over 30 years old')
print('sorry, you do not qualify')
# if you this its going to print last line no matter what the condition is


user_age = int(input("what is your age? "))
if user_age > 30:
    print('you are over 30 years old')
    print('sorry, you do not qualify')
else:
    print('you are 30 years old or younger')
    print('Congrats, you qualify')



if condition_a_met: # this is the basic alghoritm
    do_scenerio_a()
elif condition_b_met:
    do_scenerio_b()
elif condition_c_met:
    do_scenerio_c()
else:
    do_scenerio_d()