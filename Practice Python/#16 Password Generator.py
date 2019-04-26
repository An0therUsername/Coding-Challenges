#Exercise 16 (and Solution)

'''Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.'''

import string
import clipboard
from secrets import choice
alphabet = string.ascii_letters + string.digits + string.punctuation

def generate_password(length):
    password = ''.join(choice(alphabet) for i in range(length))
    return password

def reply(password):
    clipboard.set(password)
    print('Your new password is:\n')
    return password + '\t (copied to clipboard)\n'
   
while True:
    answer = input('Shall I create a new password for you? (y)es or (n)o: ')
    if answer == 'n':
        print('Goodbye')
        break
    else:
        pw_length = input('How long shall your password be? Please enter the number of digits: ')
        print(reply(generate_password(int(pw_length))))
        continue
        

