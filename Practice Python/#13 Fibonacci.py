#Exercise 13 (and Solution)

'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''

def get_number(prompt):
    return int(input(prompt))
    
def build_fib(repeats):
    fib_sequence = [1, 2]
    if repeats == 0:
        fib_sequence = []
    elif repeats == 1:
        fib_sequence = [1]
    elif repeats == 2:
        fib_sequence = [1,2]
    elif repeats > 2:
        while True:
            x = fib_sequence[-2] + fib_sequence[-1]
            fib_sequence.append(x)
            if len(fib_sequence) == repeats:
                break
    return fib_sequence

def reply(fib_sequence):
    print('Here is your sequence: ' + str(fib_sequence))
    
reply(build_fib(get_number('How many Fibonnaci numbers shall I generate? ')))
