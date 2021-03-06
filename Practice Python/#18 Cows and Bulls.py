'''Exercise 18 (and Solution)

Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.'''

#######

import random

def create_number():
    '''
    Create random 4 digit number
    '''
    numbers = list(range(10))
    random.shuffle(numbers)
    
    master = ''
    for i in range(4):
        master += str(numbers[i])

    return master

def user_input():
    '''
    Ask for users 4 digit guess
    '''
    while True:
        guess = input("\nWhat's your guess? ")
        wrong = False
        for i in guess:
            if i not in '0123456789':
                wrong = True
                break 
        if wrong == True:
            print('\nPlease enter digits.')
        elif len(guess) != 4:
            print('\nPlease enter FOUR digits')
        else:
            return guess   
    
def give_clue(master, guess):
    '''
    Give feedback on guess
    '''
    bull = 0
    cow = 0
    
    if guess == master:
        print('You got it!')
        
    for i in range(len(guess)):
        if guess[i] == master[i]:
            cow += 1
        elif guess[i] in master:
            bull += 1
        
    if cow != 0 or bull != 0:
        print(str(cow) + ' Cows, ' + str(bull) + ' Bulls')
    else:
        print('Bananas')

print('Cows and Bulls')
print('='*48)
print('I am thinking of a 4-digit number with no double digits. Try to guess what it is.' )
print('Here are some clues:\n')
print('When I say:    That means:')
print('  Bull         One digit is correct but in the wrong position.')
print('  Cow          One digit is correct and in the right position.')
print('  Bananas      No digit is correct.\n')

while True:
    '''
    Main game loop
    '''
    tries = 0
    master = create_number()
    
    while True:
        guess = user_input()
        give_clue(master, guess)
        tries += 1
        
        if master == guess:
            break
    
    print('\nCongratulations! It took you ' + str(tries) + ' tries.')
    
    # Ask player if thye want to play again.
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
