from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv, requests
import datetime

# specify the url
URL = 'http://www.bloomberg.com/quote/SPX:IND'
print(URL)
page = requests.get(URL)
plain_text = page.text
soup = BeautifulSoup(plain_text, features='html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('section')
print(str(name_box))

name = name_box.text.strip()
# strip() is used to remove starting and trailing spaces
print(name)

# get the index price
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print(price)

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.datetime.now().date()])