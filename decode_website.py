'''
Exercise 17: Decode a webpage

Use the BeautifulSoup and requests Python packages
to print out a list of all the article titles on the
New York Times homepage (https://www.nytimes.com/).

Suggested libraries: requests, BeatifulSoup
'''

import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
response = urllib.request.urlopen(url)
r_html = response.read()
titles = []
soup = BeautifulSoup(r_html, features='html.parser')
for title in soup.find_all("div", {"class": "css-debyuq e1voiwgp1"}):
    print(title.text)

