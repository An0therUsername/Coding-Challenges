"""Exercise 6 (and Solution)

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)"""

word = input("Please enter a word and I will determine if it is a palindrome: ")
word_list = list(word)
word_rev = list(word)
word_rev.reverse()

if word_list == word_rev:
    print("The word '" + word.upper() + "' is a palindrome and can be spelled forwards and backwards.")
else:
    print("The word '" + word.upper() + "' is spelled " + str(word_rev) + " backwards and is not a palindrome.")
