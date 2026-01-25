#Exercise 010 - Write a program that reads how much money a person has in their wallet and show how many dollars they can buy.
real = float(input('How much money do you have in your wallet? '))
dollar = real / 3.27
print('you can buy {} dollars'.format(dollar))