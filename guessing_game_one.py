'''
Exercise 9: Guessing Game One

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed
too low, too high, or exactly right.
'''

import random

user_exit = 0
comp_num = random.randint(1,9)
local_guess_count = 0
total_guess_count = 0

print('''Let's play a guessing game!\n
I will pick a number between 1 and 9 and you will guess until you get it.
Remember: you can enter \"exit\" if you would like to stop at any time.
...
Alright, I have chosen my number!
''')

while user_exit < 1:
    user_input = input("What is your guess? \n ")
    if user_input == "exit":
        total_guess_count = total_guess_count + local_guess_count
        print("Sorry to see you go! (FYI, you made " + str(total_guess_count) + " guesses in total)")
        user_exit = 1
        break
    try:
        user_num = int(user_input)
        if int(user_num) == comp_num:
            print("Your is guess right! My number was", comp_num)
            again = input("Do you want to play again? (enter \"yes\" to play again): ")
            local_guess_count = local_guess_count + 1
            total_guess_count = total_guess_count + local_guess_count
            if again == "yes":
                comp_num = random.randint(1,9)
                local_guess_count = 0    
            else:
                print("Good game! (FYI, it took you " + str(local_guess_count) + " guesses on this round, and you made " + str(total_guess_count) + " guesses in total!)")
                user_exit = 1
    
        elif int(user_num) < comp_num:
            print("Sorry, your guess was too low!")
            local_guess_count = local_guess_count + 1
        elif int(user_num) > comp_num:
            print("Sorry, your guess was too high!")
            local_guess_count = local_guess_count + 1

    except ValueError:
            print("I am not sure what you wrote...so I will end the game.")
            user_exit = 1
    
