#Exercise 018 - Write a program that reads any angle and displays the sine, cosine, and tangent of that angle on the screen.

import math

a = float(input('Enter an angle: '))
sin = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))

print('Angle: {:.2f}°\nSin: {:.2f}\ncos: {:.2f}\ntg: {:.2f}'.format(a,sin,cos,tg))
