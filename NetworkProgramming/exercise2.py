from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

number = 0
total = None

# Retrieve span tags
tags = soup('span')

for tag in tags :
    x = tag.contents[0].strip()
    try :
        y = int(x)
        if number == 0 :
            total = y
        else :
            total = total + y
        number = number + 1
    except :
        continue

print('Count', number)
print('Sum', total)
