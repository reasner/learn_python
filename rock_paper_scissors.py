'''
Exercise 8: Rock, Paper, Scissors

Make a two-player Rock-Paper-Scissors game.
'''
import random

user_start = input('Would you like to play rock, paper, scissors with me? (y/n): ' )
if user_start == 'y':
    print("Great! First to three wins!")
    user_tally = 0
    comp_tally = 0
    while user_tally < 3 and comp_tally < 3:
        user_move = input('Pick your move: rock (r), paper (p), or scissors (s): ' )
        #random.seed(1234)
        comp_draw = random.random()
        if comp_draw < 0.33:
            comp_move = 'r'
        elif comp_draw >= 0.33 and comp_draw < 0.66:
            comp_move = 'p'
        elif comp_draw >= 0.66 and comp_draw <= 1:
            comp_move = 's'
            
        if user_move != 'r' and user_move != 'p' and user_move != 's':
            print('I cannot play if you cannot follow directions!')
            
        if user_move == comp_move:
            print('We both picked ' + user_move + ', it\'s a draw')
        elif (user_move == 'r' and comp_move == 's') or (user_move == 'p' and comp_move == 'r') or (user_move == 's' and comp_move == 'p'):
            print('Shucks, you won by picking ' + user_move + ' when I picked ' + comp_move)
            user_tally = user_tally + 1
            print("Your tally is: " + str(user_tally))
            print("My tally is: " + str(comp_tally))
        elif (comp_move == 'r' and user_move == 's') or (comp_move == 'p' and user_move == 'r') or (comp_move == 's' and user_move == 'p'):
            print('Looks like I won by picking ' + comp_move + ' when you picked ' + user_move)
            comp_tally = comp_tally + 1
            print("Your tally is: " + str(user_tally))
            print("My tally is: " + str(comp_tally))
            
    if user_tally == 3:
        print("You win! Good game.")
    elif comp_tally == 3:
        print("Haha, I won!")

elif user_start == 'n':
    print('Okay, I will play by myself!')
else:
    print('You\'re not very good at following instructions... no game for you then!')
