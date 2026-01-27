#Exercise 020 -  The Same teacher from challenge 019 wants to ramdomly select the order in which studens will present their work. Create a program that reads the names of four studens and displays the randomly selected order.

from random import sample

a1 = str(input("1st student's name: "))
a2 = str(input("2nd student's name: "))
a3 = str(input("3rd student's name: "))
a4 = str(input("4th student's name: "))

chosen = sample([a1, a2, a3, a4],k=4)

print(chosen)