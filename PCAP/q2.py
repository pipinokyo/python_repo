# What snippet would you insert in the line indicated below:
n = 0
while n < 4:
    n += 1
    # insert your code here

# to print the following string to the monitor after the loop finishes its execution:
1 2 3 4

A. print(n)
B. print(n, sep=” “)
C. print(n, end=” “)
D. print(n, ” “)

'''
Understanding the Loop:



Initialization: n = 0
Loop Condition: while n < 4
The loop will run as long as n is less than 4.
Loop Body: n += 1
Inside the loop, n is incremented by 1 in each iteration.

Loop Execution:
Let's visualize how n changes in each iteration:

Iteration	    n before n += 1	      n after n += 1
    1	                0	                   1           
    2	                1	                   2
    3	                2	                   3
    4	                3	                   4
After the 4th iteration, n becomes 4, so the condition n < 4 is False, and the loop exits.

At this point, n = 4

Option A: print(n)
This would simply print the current value of n, which is 4.
Output: 4
(Not the desired 1 2 3 4)

Option B: print(n, sep=" ")
sep is used to separate multiple arguments passed to print. Here, only one argument (n) is passed, so sep has no effect.
Output: 4
(Same as Option A, not desired)


Option C: print(n, end=" ")


Option D: print(n, " ")
This prints n (which is 4) and a space " ", separated by a space (default sep).
Output: 4
(Not desired)

'''