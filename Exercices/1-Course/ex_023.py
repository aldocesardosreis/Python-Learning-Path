#Exercise 023 - Write a program that reads a number from 0 to 9999 and diaplays each of its digits separately on the screen.

n = int(input("Enter a number from 0 to 9999: "))
n1 = str("{:04}".format(n))
print("Number {}\n units: {}\n tens: {}\n hundreads: {}\n thousands: {}".format(n1, n1[3], n1[2], n1[1], n1[0]))
