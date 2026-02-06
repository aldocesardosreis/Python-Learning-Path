#Exercise 026 - Write a program that reads a sentence from the keyboard and displays how many times the letter "A" appears, its first last position.

phrase = str(input("Enter a phrase: ")).strip()
count = (phrase.upper()).count("A")
appearsf = (phrase.upper()).find("A")
appearsl = (phrase.upper()).rfind("A")

print("The letter 'A' appears {} times\nAppears at first in {} position\nAppears at least in {} position".format(count, appearsf+1, appearsl+1))
