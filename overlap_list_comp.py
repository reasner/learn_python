'''
Exercise 10: List Overlap Comprehensions

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	
and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
Write using at least one list comprehension.

Extra:
Randomly generate two lists to test this

'''

import random

length_list_1 = random.randint(1,50)
length_list_2 = random.randint(1,50)

list_1 = random.sample(range(100), length_list_1)
list_2 = random.sample(range(100), length_list_2)

overlap = [a for a in set(list_1) if a in list_2]
print(overlap)

