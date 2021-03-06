#! Problem 2

'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

#initialize lists
fib_sequence = [1,2]
even_fib_sequence = []

#build fibonacci sequence
while True:
    x = fib_sequence[-2] + fib_sequence[-1]
    if x >= 4000000:
        break
    else:
        fib_sequence.append(x)

#build sequence with even numbers  
for x in fib_sequence:
        if x % 2 == 0:
            even_fib_sequence.append(x)

#add up even numbers in sequence
print(sum(even_fib_sequence))
