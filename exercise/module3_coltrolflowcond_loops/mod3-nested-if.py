answer_a = input('Do you like travelling? y/n: ')
if answer_a == 'y':
    answer_b = input('And do you like Asia? y/n: ')
    if answer_b == 'y':
      print('Excellent! You can win a ticket to Thailand!')
    else:
      print('Sorry to hear that!')
else:
    print('Sorry to hear that!')


# Do you like travelling? y/n: y
# And do you like Asia? y/n: y
# Excellent! You can win a ticket to Thailand!

# Note that proper indentation is very, very important here.
# The lines with the if and else keywords in the nested if are indented with four spaces 
# but the if and else blocks are indented even further with eight spaces.