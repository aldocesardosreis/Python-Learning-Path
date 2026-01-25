#Exercise 014 - Write a program that converts a temperature entered in degrees Celsius to degrees Fahrenheit

c = float(input('Enter the temperature in Celsius: '))
f = (c * 1.8 ) + 32

print('The temperature in Fahreheit is {:.2f} °F'.format(f))