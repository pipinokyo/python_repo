# What is the expected output of the following snippet?
i = 250
while len(str(i)) > 72:
    i *= 2
else:
    i //= 2
print(i)

'''
visulation and 
1- Start:
    i = 250
    len(str(250)) = 3
    Is 3 > 72? No → Skip loop, go to else
2-Else:
    i = 250 // 2 = 125
3-Print:
    Output: 125
'''