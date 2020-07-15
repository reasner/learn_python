'''
Exercise 16: Password Generator

Write a password generator in Python.
Be creative with how you generate passwords
- strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password
every time the user asks for a new password.
Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be.
For weak passwords, pick a word or two from a list.
'''


#Modules
import random as rand
import string

#Functions
def def_strength_opt():
    options = ['weak','medium','strong']
    return options

def ask_for_strength(options):
    user_input = input("What strength password would you like me to generate? (Enter: " + options[0] +", " + options[1] + ", or " + options[2] + ") \n")
    return user_input.replace(" ","").lower()

def password_generator(options,strength='unk'):
    #Definitions
    upp = string.ascii_uppercase
    low = string.ascii_lowercase 
    dig = string.digits 
    punc = string.punctuation 
    mpl = 10
    spl = 20
    weak_words = ['password', 'music', 'puppy', 'love', 'python']
    num_weak_words = len(weak_words)

    #Make choice about default
    if strength == 'unk':
        print("I couldn't tell what strenght you wanted to I'll default to a " + options[0] + " password.")
        strength = options[0]

    #Option #1     
    if strength == options[0]:
        draw = rand.randint(1,num_weak_words)
        password = weak_words[draw-1]

    #Option #2    
    elif strength == options[1]:
        password = 'x'*mpl
        passlist = list(password)
        for i in range(mpl):
            if i == 0:
                draw = rand.randint(1,len(punc))
                passlist[i] = punc[draw-1]
            elif i == 1:
                draw = rand.randint(1,len(upp))
                passlist[i] = upp[draw-1]
            elif i > 1 and i < 8:
                draw = rand.randint(1,len(low))
                passlist[i] = low[draw-1]
            else:
                draw = rand.randint(1,len(dig))
                passlist[i] = dig[draw-1]
        sep = ""
        password = sep.join(passlist)
        
    #Option #3
    elif strength == options[2]:
        password = 'x'*spl
        passlist = list(password)
        for i in range(spl):
            draw = rand.randint(1,4)
            if draw == 1:
                draw = rand.randint(1,len(punc))
                passlist[i] = punc[draw-1]
            elif draw == 2:
                draw = rand.randint(1,len(upp))
                passlist[i] = upp[draw-1]
            elif draw == 3:
                draw = rand.randint(1,len(low))
                passlist[i] = low[draw-1]
            elif draw == 4:
                draw = rand.randint(1,len(dig))
                passlist[i] = dig[draw-1]
        sep = ""
        password = sep.join(passlist)

    #Output         
    return password

    
#Script
pass_str_opt = def_strength_opt()
user_strength = ask_for_strength(pass_str_opt)

if user_strength in pass_str_opt:
    new_pass = password_generator(pass_str_opt, user_strength)
else:
    new_pass = password_generator(pass_str_opt)

print("You're new password is: \n" + new_pass)
