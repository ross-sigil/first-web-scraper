'''
Jul 24, 2016

!~!~!NOW WORKING!~!~!
     Web Scraper

|----------------|
|***Objectives***|
|----------------|
1: Search Given Webpage
2: Gather Specific Data
3: Store Data

Example syntax of target webpage

http://nameberry.com/search?page=1&per_page=30&starts_with=A

http://nameberry.com/search?page=2&per_page=30&starts_with=A

http://nameberry.com/search?page=1&per_page=30&starts_with=B

http://nameberry.com/search?page=2&per_page=30&starts_with=B
'''

import lxml
from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup

opener = '/babyname/'
s = ''
z = 1
t = 0
#t is a value testing how many names are gathered per page
i = 0
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while i < 25:
    t = 0
    babyNamePage = "http://nameberry.com/search?page=" + str(z) + '&per_page=30&starts_with=' + alpha[i]
    html = urlopen(babyNamePage)
    soup = BeautifulSoup(html, "lxml")
#create link based on website syntax, then parse to html

    for link in soup.find_all('a'):
        if opener in link.get('href'):
#searchest for all href on page if /babyname/ found then adds link to string

            s += link.get('href')[10:]
            s += ' '
            t += 1
    z += 1
    if t == 0:
        i += 1
        z = 1
#loops through all pages till 0 names found, then increments i to next letter of alpha
print(s)
