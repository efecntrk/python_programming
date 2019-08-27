'''
#guessing game

-get a random number between 1 and 10
-prompt the user for to guess the number-
-loop while the user guess is not equal to your number
    if the users guess is less than the number print 'too small'
    if the users guess is greater than the number print'too big'
= print 'you are correct when the user gets the number right'


    get a random number
    
        while True: 
            ask for guess
            if the guess < number 
                print('too small')
            if the guess >:
                print('too big')
            else:
                print('you are correct....')   

                break

guess       7

number      3

too big

guess

'''

import random
guess = []

#number = int(random.randint(1, 10))

number = 5
while True:
    guess = int(input('Enter your guess: '))
    if guess > number:
        print('Too big')
    elif guess < number:
        print('Too small')
    else:
        print('You are correct')
        break
