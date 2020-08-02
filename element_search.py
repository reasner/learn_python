'''
Exercise 20: Element Search

Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not the given
number is inside the list and returns (then prints) an
appropriate boolean.

Extras:

Use binary search.
'''

#Import modules
import random

#Functions
def rand_sorted_list(list_len):
    randlist = []
    for i in range(list_len):
        randlist.append(random.randint(1,1000))
    sortlist = sorted(randlist)
    return sortlist

def ask_for_length():
    length = input("Please provide an integer to determine the length for our list: ")
    return length

def ask_for_search():
    number = input("Please provide the number you would like to search for: ")
    return number

def element_search(ulist,unum):
    search = 0
    while search == 0:
        listlen = len(ulist)
        middle = round(listlen/2)
        if listlen != 1:
            if int(unum) == ulist[middle]:
                search = 1
                didnotfind = 0
            elif int(unum) < ulist[middle]:
                ulist = ulist[:middle]
            elif int(unum) > ulist[middle]:
                ulist = ulist[middle:]
        elif listlen == 1:
            if int(unum) == ulist[0]:
                didnotfind = 0
                search = 1
            else:
                didnotfind = 1
                search = 1  
    if didnotfind == 0:
        found = True
    elif didnotfind == 1:
        found = False
    return found
        
#Script
user_len = int(ask_for_length())
ordered_list = rand_sorted_list(user_len)
print("The list I have generated for you: \n")
print(ordered_list)
user_num = ask_for_search()

found = element_search(ordered_list,user_num)
print(found)
if found is True:
    founditstr = "I found it! Your number, " + str(user_num) + ", is in the list!"
    print(founditstr)
elif found is False:
    didnotfindstr = "Sorry! I couldn't find your number, " + str(user_num) + ", in the list."
    print(didnotfindstr)  
    
