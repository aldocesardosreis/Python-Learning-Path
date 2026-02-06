#Exercise 024 - Create a program that reads the name of a city and tells whether or not it starts with the name "SANTO"

city = input("Type a city's name: ")
c = ((city.strip()).upper()).find('SANTO')

if c == 0:
    print("The city's name starts with SANTO")
else:
    print("The city's name doesn't start with SANTO")



#Resolution
#city = str(input("Type a city's name: ")).strip()
#print(city[:5].upper() == "SANTO" )
