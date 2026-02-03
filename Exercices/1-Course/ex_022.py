# Exercise 022 - Write a program that reads a person's full name and displays: the name with all uppercase and lowercase letters.
# The name with all uppercase and lowercase letters.
# The total number of letters (excluding spaces).
# The number of letters in the first name.

name = input("Write your full name: ")
namesplit = name.split()
nameletters = len(name) - name.count(' ')
firstname = namesplit[0]
firstnameletters = len(firstname)
print('Full name: {}, {}\nTotal of letters:{}\nHow many letter has the first name: {}'.format(name.upper(),name.lower(), nameletters, firstnameletters))

