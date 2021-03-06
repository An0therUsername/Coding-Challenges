'''Exercise 9 (and Solution)

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''

from random import randint

while True:

    #Get input
    computer = randint(1,9)
    print('\nGuess the number I am thinking of between 1 and 9. Press (exit) to end.')
    guesses = 0

    while True:
    #Guessing loop
        player = input('You answer: ')
        if player == 'exit':
            print('bye')
            break 
        elif int(player) < computer:
            print('try higher')
            guesses += 1
            continue 
        elif int(player) > computer:
            print('try lower')
            guesses += 1
            continue 
        elif int(player) == computer:
            guesses += 1
            print('You got it. Took you ' + str(guesses) + ' tries. Again?')
            break
    
    if player == 'exit':
            break
