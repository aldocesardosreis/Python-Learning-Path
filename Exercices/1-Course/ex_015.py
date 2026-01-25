#Exercise 015 - Write a program that asks for the number of kilometers driven by a rental a car and the number of days it was rented. Calculate the price to pay, knowing that the car costs R$ 60.00 per day and R$0.15 per kilometer driven.

days = int(input('Enter the number of the days rented: '))
d = float(input('Enter the number of the distance driven (km): '))
rent = (days*60)+(d*0.15)

print('The price to pay is R$ {:.2f}.'.format(rent))
