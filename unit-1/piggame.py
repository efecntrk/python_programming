
import random


roll = random.randint(1,6)
'''

# current_score = random.randint(1,6)
roll = random.randint(1,6)
current_score = 0

turn = 0

total_score = 0

player1_total = []

player2_totla = []
'''
'''
command = ""
turns = 0
totalScore = 0
turnScore = 0

while totalScore < 25:
    print("Turn: {} Score: {} in {} turns.".format(turnScore, totalScore, turns))
    command = input("command> ").lower()

    if command == "roll":
        roll = random.randint(1,6)
        if roll == 1:
            print("You rolled a 1! Poor you.")
            turnScore = 0
            turns = turns + 1
        else:
            #REMOVED print
            turnScore = turnScore + roll
    elif command == "hold":
        print("You've ended your turn.")
        totalScore = totalScore + turnScore
        turnScore = 0
        turns = turns + 1
    elif command == "quit":
        print("Bye!")
        break
    else:
        print("What?")

print("FINAL SCORE: {} in {} turns ({})".format(totalScore, turns, totalScore/turns))

# Added for writing the score
if totalScore > 25:
    name = input("Winner! Enter your name: ")
    with open("scoreboard.txt", "w") as f:
        f.write("{}//{}//{}\n".format(name, turns, totalScore))




