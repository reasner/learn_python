'''
Exercise #1: Character Input

1. Create a program that asks the user to enter their name and their age.
2. Print out a message addressed to them that tells them the year that they
will turn 100 years old.
'''

name = input("What is your name? ")
age = input("What is your age? ")
birthday_yet = input("Have you had your birthday yet this year? (y/n) ")
if birthday_yet == "y":
    by = 0
elif birthday_yet == "n":
    by = 1

year100 = 2120 - int(age) - by

print(name + "," + " you will turn 100 years old in the year " + str(year100))
