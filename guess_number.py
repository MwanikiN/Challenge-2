#Python project to guess a number that has randomly been selected

import random as rand
num = rand.randint(0,100)
def guess_number(num):
    guessed_number = int(input('Guess the selected number: '))

    if guessed_number!=num:
        if guessed_number<num:
            print('Lower guess, try again?')
            return  guess_number(num)
        elif guessed_number>num:
            print('Higher guess. Try again')
            return guess_number(num)
        else:
            return guessed_number
    

guess_number(num)
print("Correct!")