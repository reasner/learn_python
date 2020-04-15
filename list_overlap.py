'''
Exercise 5: List Overlap

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''

print("A program that determines the overlap in two lists!")

list_one_input = input("Please provide your first list of numbers (comma-separated): ")
print(" ")
list_two_input = input("Please provide your first list of numbers (comma-separated): ")

list_one_str = list_one_input.split(",")
list_two_str = list_two_input.split(",")

overlap = []

for i in list_one_str:
    for j in list_two_str:
        if i == j:
            overlap.append(j)

print(overlap)


#With random lists instead of user-input
import random
#random.seed(1234)

print("A program that determines the overlap in two RANDOM lists!")
len_list_one = input("Please provide the length you'd like for the first list: ")
len_list_two = input("Please provide the length you'd like for the second list: ")

list_one = random.sample(range(1,100),int(len_list_one))
list_two = random.sample(range(1,100),int(len_list_two))

print("First RANDOM list",list_one)
print("Second RANDOM list",list_two)

overlap = []

for i in list_one:
    for j in list_two:
        if i == j:
            overlap.append(j)

print(overlap)

