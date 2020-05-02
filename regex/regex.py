import re

file = open('regex_sum_353706.txt')
 
sum = 0

for numbers in file:
    numbers = re.findall('[0-9]+',numbers)
    for number in numbers:
        sum = sum + int(number)
print(sum)

