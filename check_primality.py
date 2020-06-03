'''
Exercise 11: Check Primality and Functions

Ask the user for a number and determine whether the number is prime or
not. (For those who have forgotten, a prime number is a number that has
no divisors.). You can (and should!) use your answer to Exercise 4 to
help you. Also, take this opportunity to practice using functions.
'''

def get_integer():
    return int(input("Please enter a number: "))

def is_prime(user_input):
    divisors = []
    for num in range(1,user_input + 1):
        remain = user_input%num
        if remain == 0:
            divisors.append(num)
    number_divisors = len(divisors)
    if number_divisors == 2:
        prime_output = str(user_input) + " is a prime number."
    else:
        prime_output = str(user_input) + " is not a prime number."
    return prime_output

user_input = get_integer()

answer = is_prime(user_input)
print(answer)
