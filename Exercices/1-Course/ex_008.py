#Exercise 008 - Write a program that reads a value in meters and displays it converted to centimeters and millimeters.
meters = float(input('Enter a value in meters: '))
centimeters = meters*100
millimeters = meters*1000
print('{:.2f} meters is {:.2f} centimeters\n{:.2f} meters is {:.2f} millimeters'.format(meters,centimeters,meters,millimeters))
    