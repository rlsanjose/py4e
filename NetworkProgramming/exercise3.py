# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = None
html = None
soup = None
count = None
position = None

while True :
    url = input('Enter URL: ')
    try :
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        break
    except :
        print("Error. Try again")

while True :
    count = input('Enter count: ')
    position = input('Enter position: ')
    try :
        count = int(count) + 1
        position = int(position) - 1
        break
    except :
        print("Error. Please enter an integer")

for i in range(count):
    print("Retrieving:", url)

    if i != 0 :
        newHtml = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(newHtml, 'html.parser')

    tags = soup('a')
    dictionarylink = tags[position]
    url = dictionarylink.get('href', None)
    name = dictionarylink.contents[0]
