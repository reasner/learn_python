'''
Exercise 13: Fibonacci

Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them. Take this opportunity to think about how you can
use functions. Make sure to ask the user to enter the number of numbers
in the sequence to generate. (Hint: The Fibonnaci seqence is a sequence of
numbers where the next number in the sequence is the sum of the previous
two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5,
8, 13, …)
'''

def get_number():
    return int(input("Please provide the length of the Fibonacci sequence you would like: "))

def fibonacci(user_input=5):
    output = []
    for i in range(user_input):
        if i ==  0:
            output = output + [1]
        elif i ==  1:
            output = output + [1]
        else:
            output = output + [output[i-2] + output[i-1]]
    return output

user_number = get_number()
fib = fibonacci(user_number)
print(fib)
