'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''

numbers = [5, 15, 10, 15, 3, 7]
times = len(numbers)
number_1 = numbers[0]
k = 17

def check(number_1):
    for number in numbers:
        addition = number + number_1
        if addition == k:
            print(str(k) + ' was found. It is ' + str(number) + ' + ' + str(number_1) + '.')
            break

for x in range(times):
    check(numbers[x])
