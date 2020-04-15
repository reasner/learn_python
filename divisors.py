'''
Exercise 4: Divisors

Create a program that asks the user for a number and then prints out
a list of all the divisors of that number.
'''

user_num = input("Please enter the number you would like the divisors of: ")

try:
    int_user_num = int(user_num)
    divisors = []
    for num in range(1,int_user_num + 1):
        remain = int_user_num%num
        if remain == 0:
            divisors.append(num)    
    print(divisors)

except ValueError:
    try:
        int_user_num = round(float(user_num))
        divisors = []
        for num in range(1,int_user_num + 1):
            remain = int_user_num%num
            if remain == 0:
                divisors.append(num)
            
        print(divisors)
    except ValueError:
        print("Sorry, not a number!")



