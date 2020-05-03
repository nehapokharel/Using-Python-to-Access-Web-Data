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

current_count =0
url = input('Enter - ')
count = int(input('Enter count:'))
position = int(input('Enter position:'))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
name =[]
while current_count < count:
    for tag in tags:
        items =  tag.text
        name.append(items)
        if name.index(name[-1]) == position - 1:
            break
        else:
            continue
    current_count += 1  
print(name[-1])