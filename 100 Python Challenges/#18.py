#Question 18
#Level 3
'''
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''

def validation(password):
    low_chars = 'abcdefghijklmnopqrstuvwxyz'
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    special_chars = '$#@'    
    lc_pass = False
    uc_pass = False
    n_pass = False
    sc_pass = False
    length_pass = False
    
    for i in password:
        if i in low_chars:
            lc_pass = True
        if i in upper_chars:
            uc_pass = True
        if i in numbers:
            n_pass = True
        if i in special_chars:
            sc_pass = True
        if i == ' ':
            return None
            
    if len(password) > 6 or len(password) < 12:
        length_pass = True
        
    if lc_pass == True and uc_pass == True and n_pass == True and sc_pass == True and length_pass == True:
        return password


#Main
passwords = input('Please enter password fo be checked for validity: ').split(',')
validPasswords = []

for password in passwords:
    if validation(password):
        validPasswords.append(password)
        
print ('\nValid passwords: ' + ','.join(validPasswords))


