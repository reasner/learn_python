'''
Exercise 2: Odd or Even

1. Ask the user for a number.
2. Depending on whether the number is even or odd, print out an appropriate
message to the user.
'''

num_input = input("Which number would you like to know is either even or odd? ")

try:
    num = int(num_input)
    num_mod = num%2
    if num_mod == 0:
        print(str(num) + " is even!")
    else:
        print(str(num) + " is odd!")
        
except ValueError:
    try:
        num = round(float(num_input))
        num_mod = num%2
        if num_mod == 0:
            print(str(num) + " is even!")
        else:
            print(str(num) + " is odd!")
    except ValueError:
        print(num_input +" is not a number!")

