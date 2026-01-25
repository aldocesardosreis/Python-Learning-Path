#Exercise 011 - Write a program that reads the width and height of aa wall in meters, calculates its area, and determines the amount of paint needed to paint it, knowing that each liter of paint covers an area of 2m².

width = float(input('Enter width in meters: '))
height = float(input('Enter height in meters: '))
area = width * height
paint = area / 2

print('The area is {:.2f}m² and you need {:.2f} liters of paint to paint the wall.'.format(area,paint))
    