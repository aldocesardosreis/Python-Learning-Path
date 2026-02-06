#Exercise 027 - Write a program that reads a person's full name and then displays the first and last names separately.

fullname = str(input("Enter your full name: ")).strip()
name = fullname.split()
lastname = (len(name))-1
print(fullname.split())

print("Your full name is {}\nYour first name is {}\nYour Last name is {}".format(fullname, name[0], name[lastname]))
