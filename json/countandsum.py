import urllib.request, urllib.parse, urllib.error
import json

#Data collection
link = input('Enter url: ')
print('Retrieving', link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    js = json.loads(html)
except:
    js = None

count = 0
sum = 0
for item in js['comments']:
    count = count + 1
    sum = sum + int(item['count'])

print('Count:', count)
print('Sum:', sum)