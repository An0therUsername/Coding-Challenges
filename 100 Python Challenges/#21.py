#Question 21
#Level 3
'''
Question
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import math

og_point = [0,0]

while True:
    command = input()
    if not command:
        break
    direction = command.split(' ')
    if direction[0] == 'UP':
        og_point[1] += int(direction[1])
    elif direction[0] == 'DOWN':
        og_point[1] -= int(direction[1])
    elif direction[0] == 'LEFT':
        og_point[0] -= int(direction[1])
    elif direction[0] == 'RIGHT':
        og_point[0] += int(direction[1])
    else:
        pass
    print(f'New position is {og_point}')

distance = math.pow(og_point[0],2) + math.pow(og_point[1],2)

print('The distance from OG is ' + str(round(math.sqrt(distance))))
