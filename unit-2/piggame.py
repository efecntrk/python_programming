'''
turn = 1
player_one_total = 0
player_two_total = 0
max_score = 20

while true
    read choice
    if choice = 'r' then 
        get the score 
        if the score is not 1
            if turn is 1
                add the score to player_one_total
            else 
                add the score to player_two_total

        else:
            if turn is 1
                player_one_score = 0
                turn = 2
            else 
                player_two_score = 0
                turn = 1

        if player_one_total >= max_score or player_two_total >= max_score then  
            exit the loop        
turn             | 1 |
player_one_total | 0 | 3 |
player_two_total | 0 |
choice           | r |
score            |   | 3 |
'''
import random


turn = 1
player_one_total = 0
player_two_total = 0
max_score = 20


while True:
    choice = input('Enter your command: ')
    if choice == 'r':
        score = random.randint(1, 6)
        
        if score != 1:
            if turn == 1:
                player_one_total += score
            else:
                player_two_total += score
        else:
            if turn == 1:
                player_one_total = 0
                turn = 2
            else:
                player_two_total = 0
                turn = 1
             
        if player_one_total >= max_score or player_two_total >= max_score:
            break
        print(player_one_total, player_two_total)
            
if player_one_total >= max_score:
    print('Player one wins')
else:
    print('Player two wins')
    
        

