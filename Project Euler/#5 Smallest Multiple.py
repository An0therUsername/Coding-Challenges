# Problem 5
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


i = 1
j = 1

numbers = [2,3,4,5,6,7,8,9,10]

while i:
    if i%2 == 0 and i%3 == 0 and i%4 == 0 and i%5 == 0 and i%6 == 0 and i%7 == 0 and i%8 == 0 and i%9 == 0 and i%10 == 0:
        print("It's " + str(i))
        break
    i += 1
  

#if i%range(1,20):
    
while j:
    if j%2 == 0 and j%3 == 0 and j%4 == 0 and j%5 == 0 and i%6 == 0 and j%7 == 0 and i%8 == 0 and j%9 == 0 and i%10 == 0 and j%11 == 0 and i%12 == 0 and j%13 == 0 and i%14 == 0 and i%15 == 0 and j%16 == 0 and j%17 == 0 and i%18 == 0 and j%19 == 0 and j%20 == 0:
        print("It's " + str(j))
        break
    j += 1
