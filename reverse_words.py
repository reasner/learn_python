''' Exercise 15: Reverse Word Order

Write a program (using functions!) that asks the user for a long
string containing multiple words. Print back to the user the same
string, except with the words in backwards order.

For example, say I type the string:

  "My name is Michele"
  
Then I would see the string:

  "Michele is name My"
  
shown back to me.
'''

def recover_words():
    raw_words = input("Please provide me words to reverse: ")
    return raw_words

def reverse_words(user_words="anything enter you didn't why"):
    user_no_punc = user_words
    bad_punc = "!@#$%^&*(),.?/~|[]1234567890;:-_+=<>"
    for char in bad_punc:
        user_no_punc = str.replace(user_no_punc,char,'')
    split_user = user_no_punc.split()
    number_words = len(split_user)
    output = ''
    for num in range(number_words):
        output = output + ' ' + split_user[-num-1]
    output = output[1:]
    return output
        
user_input = recover_words()
reversed_output = reverse_words(user_input)
print(reversed_output)
