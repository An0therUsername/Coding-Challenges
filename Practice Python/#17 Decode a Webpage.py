#Exercise 17 (and Solution)

'''Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.'''
    
import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


h2_tags = soup.findAll('h2')
for allh2 in h2_tags:
    print (allh2.text + '\n')
