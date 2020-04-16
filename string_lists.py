'''
Exercise 6: String Lists

Ask the user for a string and print out whether this string is a
palindrome or not.
'''

print('This program determines if a word is a palindrome!')

user_input = input('Please enter the word you would like to test: ')

l = len(user_input) 
reverse_user_input = user_input[::-1]
eq_test = 0

for char in user_input:
    for inv_char in reverse_user_input:
        if char == inv_char:
            eq_test = eq_test + 1
            break

if eq_test == l:
    print('Your word is a palindrome!')
else:
    print('Sorry, your word is not a palindrome!')
        
