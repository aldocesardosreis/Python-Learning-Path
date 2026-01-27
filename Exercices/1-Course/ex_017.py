#Exercise 017 - Write a program that reads the lengths of the opposite and adjacent legs of a right triangle. Calculate and display the length of the hypotenuse.

import math

a = float(input('Enter the opposite leg: '))
b = float(input('Enter the adjacent leg: '))
c = math.sqrt((a**2)+(b**2))

print('The hypotenuse is {:.2f}'.format(c))
