#Exercise 24 (and Solution)
'''This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by

  print("Thing to show on screen")
Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet, like this TutorialsPoint link.'''


def requestBoard():
    while True:
        print('Which board size would you like?')
        print('1. 3x3 (i.e. Tic Tac Toe)')
        print('2. 8x8 (i.e. Chess)')
        print('3. 19x19 (i.e. GO)')
        print('4. Custom')
        print('Please select 1,2,3 or 4')
        selection = input()
        if selection == '1':
            return (3, 3)
            break
        elif selection == '2':
            return (8, 8)
            break
        elif selection == '3':
            return (19, 19)
            break
        elif selection == '4':
            width = input('Enter custom width: ')
            height = input('Enter custom height: ')
            return (int(width), int(height))
            break


def drawBoard(boardSize):
    width = boardSize[0]
    height = boardSize[1]

    for x in range(width):
        print(' ---' * int(width))
        print('|   ' * int(height) + '|')
    print(' ---' * int(width))


drawBoard(requestBoard())

