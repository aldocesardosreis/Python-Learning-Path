#Exercise 016 - Write a program that reads any Real number from the keyboard and display its integer portion on the screen.

import math

n = float(input('Enter a real number: '))
m = math.trunc(n)
print('The integer portion of {} is {}'.format(n,m))
    