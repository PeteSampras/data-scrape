#import urllib2
#import requests as req #windows py3
import urllib.request #windows
import urllib.parse
import re
from bs4 import BeautifulSoup

#1 getting web page:
web_page = 'https://finance.yahoo.com/quote/FB?p=FB'
page = urllib.request.urlopen(web_page).read()
soup=BeautifulSoup(page,'html.parser')
#print(soup.h1)

name_box = soup.find('h1', attrs={'class': 'D(ib)'})
print(name_box)
name = name_box.text
print(name)

price_box = soup.find('span', attrs={'class': 'Fw(b)'})
price = price_box.text
print(price)

import csv
from datetime import datetime

with open('index.csv', 'a') as csv_file: 
     writer = csv.writer(csv_file) 
     writer.writerow([name, price, datetime.now()]) 



     