#Exercise 006 - Create an algorithm that reads a number and displays its double, triple and square root
n1 = float(input('Type an number: '))
x2 = n1 * 2
x3 = n1 * 3
squareroot = n1**(1/2)
print('The double of {:.2f} is {:.2f}\nThe triple of {:.2f} is {:.2f}\nThe square root of {:.2f} is {:.2f}'.format(n1,x2,n1,x3,n1,squareroot))
    