# What is the expected output of the following code?

def func(x):
    try:
        x = x / x
    except:
        print('a', end='')
    else:
        print('b', end='')
    finally:
        print('c', end='')

func(1)
func(0)