#Exercise 15 (and Solution)

'''Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.'''

def ask_user():   
    return input('I am Reversi 3000! Please enter a sentence: ')

def convert_string_to_list(string):
    elements = list(string.split(' '))
    return elements
    
def reverse_order(l):
    return l[::-1]

def convert_list_to_string(l):
    rev_sentence = ' '.join(map(str,l))
    return rev_sentence
    
def output(rev_sentence):
    print(rev_sentence)

output(
    convert_list_to_string(
        reverse_order(
            convert_string_to_list(
                ask_user()))))
