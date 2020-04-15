'''
Exercise 3: List less than 5

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that
are less than 5.
'''

lst_input = input("Please enter a list of numbers to determine which unique elements" \
      "are less than 5 (comma-seperated): " )
user_lst = lst_input.split(",",)
#user_int = map(int,user_lst)
#user_int_lst = list(user_int)
lst_output = []

for num in user_lst:
    if int(num) < 5:
        lst_output.append(num)

print(lst_output)
