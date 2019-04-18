'''Exercise 8 (and Solution)

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock'''

#Slightly modified for Player vs Computer

from random import randint

while True:

    #Get input
    computer = randint(1,3)
    player = input('\nPlease play Rock, Paper, Scissor. Press (q) to end. \nYou answer: ')

    #Calc Winner
    if player == 'rock' or player == 'Rock':
        if computer == 1:
            print('I have Rock. Draw')
        elif computer == 2:
            print('I have Paper. I win')
        elif computer == 3:
            print('I have Scissors. You win')
            
    if player == 'paper' or player == 'Paper':
        if computer == 1:
            print('I have Rock. You win')
        elif computer == 2:
            print('I have Paper. Draw')
        elif computer == 3:
            print('I have Scissors. I win')
            
    if player == 'Scissors' or player == 'scissors':
        if computer == 1:
            print('I have Rock. I win')
        elif computer == 2:
            print('I have Paper. You win')
        elif computer == 3:
            print('I have Scissors. Draw')
            
 #terminate session    
    if player == 'q':
        print('bye')
        break
