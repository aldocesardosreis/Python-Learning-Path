#Exercise 023 - Write a program that reads a number from 0 to 9999 and diaplays each of its digits separately on the screen.

n = int(input("Enter a number from 0 to 9999: "))
n1 = ("{:04}".format(n))
numbers = str(n1.split())
print("{}\n units: \n tens: \n hundreads: \n thousands: ".format(n1))
print(numbers[3]) 
print(numbers[2]) 
print(numbers[1]) 
print(numbers[0])