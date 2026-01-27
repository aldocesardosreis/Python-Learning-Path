#Exercise 019 - A teacher wants to randomly select one of this four students to erase the whiteboard. Write a program that helps him by reading the student's names and displaying the name of the chosen student on the screen.

import random

a1 = str(input("Enter the 1st student's name :"))
a2 = str(input("Enter the 2nd student's name :"))
a3 = str(input("Enter the 3rd student's name :"))
a4 = str(input("Enter the 4th student's name :"))
n = random.randint(1, 4)

if n == 1:
    print("The chosen student is {}".format(a1))
elif n == 2:
    print("The chosen student is {}".format(a2))
elif n == 3:
    print("The chosen student is {}".format(a3))
elif n == 4:
    print("The chosen student is {}".format(a4))
else:
    print("Error")
