'''
Exercise 14: List Remove Duplicates

Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing
a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a
different function.

Exercise 5 compares the follow lists and then two random lists:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''

import random

def request_numbers():
    user_str_input = input("Please enter a list of numbers seperated by commas: ")
    try:
        user_num_input = list(map(int, user_str_input.split(','))) 
    except ValueError:
        print("Whoopsie, I couldn't read that list... I'll give you a list instead!")
        user_num_input = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    return user_num_input  
def exercise_five_lists():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    return a, b

def gen_random_lists():
    length_one = random.randint(1, 9)
    length_two = random.randint(1, 9)
    list_one = []
    list_two = []
    for x1 in range(length_one):
        list_one.append(random.randint(1,20))
    for x2 in range(length_two):
        list_two.append(random.randint(1,20))
    return list_one, list_two

def duplicates_drop():
    pass

def duplicates_drop_loop(usr_inp):
    unique_list = []
    for number in usr_inp:
        if number not in unique_list:
                unique_list.append(number)
    return unique_list
    
def duplicates_drop_set(usr_inp):
    usr_inp_set = set(usr_inp)
    return usr_inp_set

def unique_two_lists(usr_inp_a,usr_inp_b):
    comb_list = usr_inp_a + usr_inp_b
    comb_set = set(comb_list)
    uniq_list = list(comb_set)
    return uniq_list

user_input = request_numbers()
loop_output = duplicates_drop_loop(user_input)
print("Unique values by loop: ")
print(loop_output)
set_output = duplicates_drop_set(user_input)
print("Unique values by set: ")
print(set_output)
e5a, e5b = exercise_five_lists()
print("Fixed lists to find unqiue values between: ")
print(e5a)
print(e5b)
r5a,r5b = gen_random_lists()
print("Random lists to find unqiue values between: ")
print(r5a)
print(r5b)
uniq_fixd = unique_two_lists(e5a,e5b)
print("Unique values from fixed lists: ")
print(uniq_fixd)
uniq_rand = unique_two_lists(r5a,r5b)
print("Unique values from random lists: ")
print(uniq_rand)
