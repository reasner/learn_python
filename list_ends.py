'''
Exercise #12: List Ends

Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25]) and makes a new list of only the
first and last elements of the given list. For practice,
write this code inside a function.
'''

def list_ends(user_str= '5,10,15,20,25'):
    user_list = user_str.split(',')
    list_begin = int(user_list[0])
    list_end = int(user_list[-1])
    output = [list_begin,list_end]
    return output

def get_list():
    return str(input("Please enter a list of numbers separated by commas: "))

user_input = get_list()
result = list_ends(user_input)
print(result)

