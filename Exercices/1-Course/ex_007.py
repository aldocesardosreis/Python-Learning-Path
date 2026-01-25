#Exercise 007 - Develop a program that reads a student's two grades, calculates their average, and displays it
n1 = float(input('Enter the first grade: '))
n2 = float(input('Enter the second grade: '))
average = (n1+n2)/2
print('The average of the student is {:.1f}'.format(average))