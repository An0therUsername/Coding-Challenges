#Exercise 21 (and Solution)
'''
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.'''

import requests
from bs4 import BeautifulSoup
from datetime import date

date = date.today()

print('New York Times Headlines - File Export')
print('*'*40)

#Bonus
getFileName = input('Do you want to name the file? y/n')
while True:
    if getFileName == 'y':
        custom_name = input('Please enter file name: ')
        file = f'{custom_name}.txt'
        break
    elif getFileName == 'n':
        file = f'headlines {date}.txt'
        break
    else:
        print('Please reply with (y)es or (n)o.')
        getFileName = input('Do you want to name the file? y/n')
#

print('\nfetching your headlines...')

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


h2_tags = soup.findAll('h2')

with open(file, 'w') as fileobject:
    fileobject.write("Today's Headlines:\n")
    for line in h2_tags:
        fileobject.write(line.text.encode('ascii', 'ignore').decode('ascii') + '\n')
    fileobject.
    

print(f'Operation complete. File {file} created')
