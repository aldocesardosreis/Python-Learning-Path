#Exercise 012 - Write an algorithm that reads the price of a product and displays its new price with a 5% discount.

price = float(input("Enter the product's price: R$ "))
priceoff = price * 0.95

print('the new price is R$ {:.2f}'.format(priceoff))
